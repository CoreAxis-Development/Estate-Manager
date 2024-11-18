import psutil
import logging

logger = logging.getLogger(__name__)

class SystemStatsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get system stats
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        disk_usage = psutil.disk_usage('/')
        net_io = psutil.net_io_counters()

        # Log the stats
        logger.info(f"CPU Usage: {cpu_usage}%")
        logger.info(f"Memory Usage: {memory_info.percent}%")
        logger.info(f"Disk Usage: {disk_usage.percent}%")
        logger.info(f"Bytes Sent: {net_io.bytes_sent}")
        logger.info(f"Bytes Received: {net_io.bytes_recv}")

        response = self.get_response(request)
        return response