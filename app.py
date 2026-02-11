import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import threading
import json
from datetime import datetime

from src.core.scanner import NetworkScanner
from src.utils.network_utils import parse_target, parse_ports
from src.core.host_discovery import HostDiscovery
from src.core.port_scanner import PortScanner

class NetworkScannerGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Network Scanner Pro v1.0")
        self.window.geometry("1400x850")
        self.window.configure(bg="#0a0e27")
        
        self.is_scanning = False
        self.results = []
        self.scan_start_time = None
        self.setup_ui()
        
    def setup_ui(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TEntry', fieldbackground="#1a1f3a", foreground="#ffffff", borderwidth=0)
        
        main_container = tk.Frame(self.window, bg="#0a0e27")
        main_container.pack(fill=tk.BOTH, expand=True)
        
        sidebar = tk.Frame(main_container, bg="#0f1324", width=400)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        sidebar.pack_propagate(False)
        
        title_label = tk.Label(
            sidebar,
            text="🔍 Network\nScanner Pro",
            font=("Helvetica", 24, "bold"),
            bg="#0f1324",
            fg="#00d9ff",
            justify=tk.LEFT
        )
        title_label.pack(anchor=tk.W, padx=25, pady=(30, 40))
        
        config_container = tk.Frame(sidebar, bg="#0f1324")
        config_container.pack(fill=tk.BOTH, padx=20, pady=(0, 20))
        
        self.create_input_field(config_container, "TARGET IP/RANGE", "192.168.1.0/24", is_target=True)
        self.create_input_field(config_container, "PORTS", "21,22,23,25,80,443,445,3389,8080")
        
        settings_frame = tk.Frame(config_container, bg="#0f1324")
        settings_frame.pack(fill=tk.X, pady=(15, 0))
        
        tk.Label(
            settings_frame,
            text="THREADS",
            bg="#0f1324",
            fg="#6c7a89",
            font=("Helvetica", 9, "bold")
        ).pack(anchor=tk.W, pady=(0, 5))
        
        self.threads_spinbox = ttk.Spinbox(settings_frame, from_=10, to=500, width=35, font=("Helvetica", 11))
        self.threads_spinbox.set(100)
        self.threads_spinbox.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(
            settings_frame,
            text="TIMEOUT (SEC)",
            bg="#0f1324",
            fg="#6c7a89",
            font=("Helvetica", 9, "bold")
        ).pack(anchor=tk.W, pady=(0, 5))
        
        self.timeout_spinbox = ttk.Spinbox(settings_frame, from_=0.1, to=5.0, increment=0.1, width=35, font=("Helvetica", 11))
        self.timeout_spinbox.set(1.0)
        self.timeout_spinbox.pack(fill=tk.X)
        
        button_container = tk.Frame(sidebar, bg="#0f1324")
        button_container.pack(fill=tk.X, padx=20, pady=(20, 0))
        
        self.scan_button = self.create_sidebar_button(button_container, "▶  Start Scan", "#00d9ff", self.start_scan)
        self.scan_button.pack(fill=tk.X, pady=(0, 12))
        
        self.stop_button = self.create_sidebar_button(button_container, "⏹  Stop Scan", "#ff4757", self.stop_scan)
        self.stop_button.pack(fill=tk.X, pady=(0, 12))
        self.stop_button.config(state=tk.DISABLED)
        
        self.save_button = self.create_sidebar_button(button_container, "💾  Save Results", "#5f27cd", self.save_results)
        self.save_button.pack(fill=tk.X, pady=(0, 12))
        
        self.html_button = self.create_sidebar_button(button_container, "📊  HTML Report", "#ff6348", self.generate_html_report)
        self.html_button.pack(fill=tk.X, pady=(0, 12))
        
        self.clear_button = self.create_sidebar_button(button_container, "🗑  Clear Results", "#2f3542", self.clear_output)
        self.clear_button.pack(fill=tk.X)
        
        self.progress = ttk.Progressbar(sidebar, mode='indeterminate')
        self.progress.pack(fill=tk.X, padx=20, pady=(30, 10))
        
        self.status_label = tk.Label(
            sidebar,
            text="Ready to scan",
            bg="#0f1324",
            fg="#6c7a89",
            font=("Helvetica", 10),
            wraplength=340
        )
        self.status_label.pack(padx=20)
        
        tk.Label(
            sidebar,
            text="v1.0 | Network Scanner Pro",
            bg="#0f1324",
            fg="#2f3542",
            font=("Helvetica", 8)
        ).pack(side=tk.BOTTOM, pady=20)
        
        main_content = tk.Frame(main_container, bg="#0a0e27")
        main_content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        stats_container = tk.Frame(main_content, bg="#0a0e27")
        stats_container.pack(fill=tk.X, padx=30, pady=30)
        
        self.total_hosts_card = self.create_stat_card(stats_container, "TOTAL HOSTS", "0", "#00d9ff")
        self.total_hosts_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))
        
        self.active_hosts_card = self.create_stat_card(stats_container, "ACTIVE HOSTS", "0", "#1dd1a1")
        self.active_hosts_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))
        
        self.open_ports_card = self.create_stat_card(stats_container, "OPEN PORTS", "0", "#ee5a6f")
        self.open_ports_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))
        
        self.scan_time_card = self.create_stat_card(stats_container, "SCAN TIME", "0s", "#a29bfe")
        self.scan_time_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        results_wrapper = tk.Frame(main_content, bg="#0a0e27")
        results_wrapper.pack(fill=tk.BOTH, expand=True, padx=30, pady=(0, 30))
        
        results_header = tk.Frame(results_wrapper, bg="#0a0e27")
        results_header.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(
            results_header,
            text="Scan Results",
            bg="#0a0e27",
            fg="#ffffff",
            font=("Helvetica", 20, "bold")
        ).pack(side=tk.LEFT)
        
        results_container = tk.Frame(results_wrapper, bg="#151b3d")
        results_container.pack(fill=tk.BOTH, expand=True)
        
        self.results_canvas = tk.Canvas(results_container, bg="#151b3d", highlightthickness=0)
        scrollbar = tk.Scrollbar(results_container, orient="vertical", command=self.results_canvas.yview)
        self.scrollable_frame = tk.Frame(self.results_canvas, bg="#151b3d")
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.results_canvas.configure(scrollregion=self.results_canvas.bbox("all"))
        )
        
        self.results_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.results_canvas.configure(yscrollcommand=scrollbar.set)
        
        self.results_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.results_canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        
        empty_state = tk.Label(
            self.scrollable_frame,
            text="👆 Click 'Start Scan' to begin\n\nEnter a target IP range and click the start button\nto discover active hosts and open ports",
            bg="#151b3d",
            fg="#6c7a89",
            font=("Helvetica", 14),
            justify=tk.CENTER
        )
        empty_state.pack(pady=100)
        self.empty_state = empty_state

    def _on_mousewheel(self, event):
        self.results_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def create_input_field(self, parent, label_text, default_value, is_target=False):
        container = tk.Frame(parent, bg="#0f1324")
        container.pack(fill=tk.X, pady=(0, 15))
        
        label = tk.Label(
            container,
            text=label_text,
            bg="#0f1324",
            fg="#6c7a89",
            font=("Helvetica", 9, "bold")
        )
        label.pack(anchor=tk.W, pady=(0, 5))
        
        entry = ttk.Entry(container, font=("Helvetica", 11))
        entry.insert(0, default_value)
        entry.pack(fill=tk.X)
        
        if is_target:
            self.target_entry = entry
        else:
            self.ports_entry = entry

    def create_sidebar_button(self, parent, text, color, command):
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg="white",
            font=("Helvetica", 12, "bold"),
            pady=14,
            relief=tk.FLAT,
            cursor="hand2",
            borderwidth=0,
            activebackground=color
        )
        return btn

    def create_stat_card(self, parent, title, value, color):
        card = tk.Frame(parent, bg="#1a1f3a", relief=tk.FLAT)
        
        title_label = tk.Label(
            card,
            text=title,
            bg="#1a1f3a",
            fg="#6c7a89",
            font=("Helvetica", 10, "bold")
        )
        title_label.pack(pady=(25, 10))
        
        value_label = tk.Label(
            card,
            text=value,
            bg="#1a1f3a",
            fg=color,
            font=("Helvetica", 36, "bold")
        )
        value_label.pack(pady=(0, 25))
        
        card.value_label = value_label
        return card

    def clear_output(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        self.results = []
        self.total_hosts_card.value_label.config(text="0")
        self.active_hosts_card.value_label.config(text="0")
        self.open_ports_card.value_label.config(text="0")
        self.scan_time_card.value_label.config(text="0s")
        
        empty_state = tk.Label(
            self.scrollable_frame,
            text="👆 Click 'Start Scan' to begin\n\nEnter a target IP range and click the start button\nto discover active hosts and open ports",
            bg="#151b3d",
            fg="#6c7a89",
            font=("Helvetica", 14),
            justify=tk.CENTER
        )
        empty_state.pack(pady=100)
        self.empty_state = empty_state

    def add_host_card(self, host, ports):
        if hasattr(self, 'empty_state') and self.empty_state.winfo_exists():
            self.empty_state.destroy()
        
        card = tk.Frame(self.scrollable_frame, bg="#1a1f3a", relief=tk.FLAT)
        card.pack(fill=tk.X, padx=25, pady=15)
        
        header = tk.Frame(card, bg="#1a1f3a")
        header.pack(fill=tk.X, padx=30, pady=(25, 20))
        
        icon_text = "🖥️" if ports else "💤"
        icon = tk.Label(header, text=icon_text, bg="#1a1f3a", font=("Arial", 28))
        icon.pack(side=tk.LEFT, padx=(0, 20))
        
        ip_label = tk.Label(
            header,
            text=host,
            bg="#1a1f3a",
            fg="#00d9ff",
            font=("Helvetica", 22, "bold")
        )
        ip_label.pack(side=tk.LEFT)
        
        if ports:
            badge = tk.Label(
                header,
                text=f"{len(ports)} port{'s' if len(ports) > 1 else ''}",
                bg="#00d9ff",
                fg="#0f1324",
                font=("Helvetica", 12, "bold"),
                padx=20,
                pady=10
            )
            badge.pack(side=tk.RIGHT)
            
            tk.Frame(card, bg="#2a2f4a", height=1).pack(fill=tk.X, padx=30, pady=(0, 25))
            
            ports_frame = tk.Frame(card, bg="#1a1f3a")
            ports_frame.pack(fill=tk.X, padx=30, pady=(0, 25))
            
            for i, port_info in enumerate(ports):
                col = i % 5
                row = i // 5
                
                port_card = tk.Frame(ports_frame, bg="#0f1324", relief=tk.FLAT)
                port_card.grid(row=row, column=col, padx=8, pady=8, sticky=(tk.W, tk.E))
                
                ports_frame.columnconfigure(col, weight=1)
                
                port_label = tk.Label(
                    port_card,
                    text=f"{port_info['port']}",
                    bg="#0f1324",
                    fg="#00d9ff",
                    font=("Helvetica", 20, "bold")
                )
                port_label.pack(anchor=tk.W, padx=18, pady=(18, 5))
                
                service_label = tk.Label(
                    port_card,
                    text=port_info['service'],
                    bg="#0f1324",
                    fg="#8892b0",
                    font=("Helvetica", 10)
                )
                service_label.pack(anchor=tk.W, padx=18, pady=(0, 18))
        else:
            no_ports_label = tk.Label(
                card,
                text="No open ports detected",
                bg="#1a1f3a",
                fg="#57606f",
                font=("Helvetica", 12, "italic")
            )
            no_ports_label.pack(pady=(0, 25))
        
        self.results_canvas.update_idletasks()
        self.results_canvas.yview_moveto(1.0)

    def start_scan(self):
        target = self.target_entry.get().strip()
        ports = self.ports_entry.get().strip()
        threads = int(self.threads_spinbox.get())
        timeout = float(self.timeout_spinbox.get())
        
        if not target:
            messagebox.showerror("Error", "Please enter a target IP or range!")
            return
        
        self.is_scanning = True
        self.scan_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.progress.start(10)
        self.status_label.config(text="🔄 Scanning in progress...", fg="#ffa502")
        self.clear_output()
        
        scan_thread = threading.Thread(
            target=self.run_scan,
            args=(target, ports, threads, timeout)
        )
        scan_thread.daemon = True
        scan_thread.start()

    def run_scan(self, target, ports, threads, timeout):
        import time
        self.scan_start_time = time.time()
        
        try:
            ip_list = parse_target(target)
            self.total_hosts_card.value_label.config(text=str(len(ip_list)))
            
            host_discovery = HostDiscovery(timeout)
            active_hosts = host_discovery.discover_hosts(ip_list)
            
            if not active_hosts:
                self.scan_complete()
                return
            
            self.active_hosts_card.value_label.config(text=str(len(active_hosts)))
            
            port_list = parse_ports(ports)
            port_scanner = PortScanner(port_list, timeout, threads)
            
            total_open_ports = 0
            
            for host in active_hosts:
                if not self.is_scanning:
                    break
                
                open_ports = port_scanner.scan_host(host)
                
                if open_ports:
                    total_open_ports += len(open_ports)
                    self.results.append({
                        "host": host,
                        "open_ports": open_ports
                    })
                
                self.window.after(0, self.add_host_card, host, open_ports)
                self.open_ports_card.value_label.config(text=str(total_open_ports))
                
                elapsed = int(time.time() - self.scan_start_time)
                self.scan_time_card.value_label.config(text=f"{elapsed}s")
            
        except Exception as e:
            import traceback
            traceback.print_exc()
        finally:
            self.scan_complete()

    def stop_scan(self):
        self.is_scanning = False
        self.status_label.config(text="⏸️ Stopping scan...", fg="#ffa502")

    def scan_complete(self):
        self.is_scanning = False
        self.progress.stop()
        self.scan_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="✅ Scan completed", fg="#1dd1a1")

    def save_results(self):
        if not self.results:
            messagebox.showwarning("Warning", "No results to save!")
            return
            
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[
                ("JSON files", "*.json"),
                ("Text files", "*.txt"),
                ("CSV files", "*.csv"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                if file_path.endswith('.json'):
                    with open(file_path, 'w') as f:
                        json.dump(self.results, f, indent=4)
                elif file_path.endswith('.csv'):
                    import csv
                    with open(file_path, 'w', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(["Host", "Port", "Service"])
                        for result in self.results:
                            for port_info in result['open_ports']:
                                writer.writerow([result['host'], port_info['port'], port_info['service']])
                else:
                    with open(file_path, 'w') as f:
                        for result in self.results:
                            f.write(f"Host: {result['host']}\n")
                            for port_info in result['open_ports']:
                                f.write(f"  Port {port_info['port']}: {port_info['service']}\n")
                            f.write("\n")
                
                messagebox.showinfo("Success", "Results saved!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {str(e)}")

    def generate_html_report(self):
        if not self.results:
            messagebox.showwarning("Warning", "No results to generate report!")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".html",
            filetypes=[("HTML files", "*.html"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                total_ports = sum(len(r['open_ports']) for r in self.results)
                
                html = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>Network Scan Report</title>
<style>*{{margin:0;padding:0;box-sizing:border-box}}body{{font-family:'Segoe UI',sans-serif;background:linear-gradient(135deg,#0a0e27,#151b3d);color:#fff;padding:40px}}.container{{max-width:1400px;margin:0 auto}}.header{{background:linear-gradient(135deg,#00d9ff,#0099cc);padding:50px;border-radius:20px;margin-bottom:40px;box-shadow:0 20px 60px rgba(0,217,255,.3)}}.header h1{{font-size:48px;margin-bottom:10px}}.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:25px;margin-bottom:40px}}.stat-card{{background:#1a1f3a;padding:35px;border-radius:15px;text-align:center}}.stat-card h3{{color:#8892b0;font-size:12px;margin-bottom:15px;text-transform:uppercase;letter-spacing:1px}}.stat-card .number{{font-size:48px;font-weight:bold}}.host-card{{background:#1a1f3a;border-radius:15px;padding:35px;margin-bottom:30px;transition:transform .3s,box-shadow .3s}}.host-card:hover{{transform:translateY(-5px);box-shadow:0 15px 40px rgba(0,217,255,.2)}}.host-header{{display:flex;justify-content:space-between;align-items:center;margin-bottom:30px;padding-bottom:20px;border-bottom:2px solid #2a2f4a}}.host-ip{{font-size:32px;font-weight:bold;color:#00d9ff}}.port-count{{background:#00d9ff;color:#0a0e27;padding:10px 25px;border-radius:25px;font-weight:bold}}.ports-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:20px}}.port-item{{background:#0f1324;padding:20px;border-radius:10px;transition:background .3s}}.port-item:hover{{background:#151b3d}}.port-number{{font-size:28px;font-weight:bold;color:#00d9ff;margin-bottom:8px}}.port-service{{color:#8892b0;font-size:14px}}</style></head><body><div class="container"><div class="header"><h1>🔍 Network Scanner Report</h1><p style="font-size:18px;opacity:.9">Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p></div><div class="stats"><div class="stat-card"><h3>Total Hosts</h3><div class="number" style="color:#00d9ff">{len(self.results)}</div></div><div class="stat-card"><h3>Hosts with Ports</h3><div class="number" style="color:#1dd1a1">{len([r for r in self.results if r['open_ports']])}</div></div><div class="stat-card"><h3>Total Open Ports</h3><div class="number" style="color:#ee5a6f">{total_ports}</div></div></div>"""
                
                for result in self.results:
                    if result['open_ports']:
                        html += f"""<div class="host-card"><div class="host-header"><div class="host-ip">🖥️ {result['host']}</div><div class="port-count">{len(result['open_ports'])} port{'s' if len(result['open_ports'])>1 else ''}</div></div><div class="ports-grid">"""
                        for port_info in result['open_ports']:
                            html += f"""<div class="port-item"><div class="port-number">{port_info['port']}</div><div class="port-service">{port_info['service']}</div></div>"""
                        html += """</div></div>"""
                
                html += """</div></body></html>"""
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(html)
                
                messagebox.showinfo("Success", "HTML report saved!")
                
                import webbrowser
                webbrowser.open(file_path)
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed: {str(e)}")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = NetworkScannerGUI()
    app.run()
