import os
import datetime


class Utils:
    @staticmethod
    def get_log_filename():
        """Generates a file name based on the current date."""
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        return f"logs_{today}.txt"

    @staticmethod
    def clean_old_logs(directory="logs", days=7):
        """Removes old logs to avoid excessive file accumulation."""
        if not os.path.exists(directory):
            os.makedirs(directory)

        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                file_date_str = filename.replace("logs_", "").replace(".txt", "")
                try:
                    file_date = datetime.datetime.strptime(file_date_str, "%Y-%m-%d")
                    if (datetime.datetime.now() - file_date).days > days:
                        os.remove(file_path)
                        print(f"🧹 Old log removed: {filename}")
                except ValueError:
                    pass


if __name__ == "__main__":
    print(Utils.get_log_filename())
    Utils.clean_old_logs()
