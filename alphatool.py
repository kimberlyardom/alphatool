import os
import subprocess
import platform

class AlphaTool:
    def __init__(self):
        self.os_type = platform.system()
        if self.os_type != "Windows":
            raise EnvironmentError("AlphaTool is designed for Windows OS.")

    def ping_test(self, host='google.com'):
        """Ping a host to check connectivity."""
        command = f"ping {host}"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode()
        error = result.stderr.decode()
        
        if result.returncode == 0:
            print(f"Ping Test Successful:\n{output}")
        else:
            print(f"Ping Test Failed:\n{error}")
    
    def flush_dns(self):
        """Flush DNS resolver cache."""
        command = "ipconfig /flushdns"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode()
        error = result.stderr.decode()
        
        if result.returncode == 0:
            print(f"DNS Cache Flushed Successfully:\n{output}")
        else:
            print(f"Failed to Flush DNS Cache:\n{error}")
    
    def check_network_adapters(self):
        """List all network adapters and their status."""
        command = "ipconfig /all"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode()
        error = result.stderr.decode()
        
        if result.returncode == 0:
            print(f"Network Adapters Info:\n{output}")
        else:
            print(f"Failed to Retrieve Network Adapters Info:\n{error}")

    def optimize_network(self):
        """Optimize network settings for better speed."""
        # Placeholder for actual implementation
        print("Network settings optimized for better speed (functionality to be implemented).")

if __name__ == "__main__":
    tool = AlphaTool()
    print("Welcome to AlphaTool: Enhancing Network Management for Windows Users")
    tool.ping_test()
    tool.flush_dns()
    tool.check_network_adapters()
    tool.optimize_network()