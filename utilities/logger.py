import datetime
import os


class Logger:

    @classmethod
    def get_log_file_path(cls):
        cur_path = os.getcwd()
        up_path = os.path.dirname(cur_path)
        logs_dir = os.path.join(os.path.abspath(up_path), "logs")
        os.makedirs(logs_dir, exist_ok=True)
        file_name = os.path.join(logs_dir, f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
        return file_name

    @classmethod
    def write_log_to_file(cls, data: str):
        try:
            filename = cls.get_log_file_path()
            with open(filename, 'a', encoding='utf=8') as logger_file:
                logger_file.write(data)
        except Exception as e:
            print(f"Failed ti write to log file: {e}")

    @classmethod
    def add_start_step(cls, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST', 'Unknown Test')

        data_to_add =  (
            f"\n-----\n"
            f"Test: {test_name}\n"
            f"Start time: {str(datetime.datetime.now())}\n"
            f"Start name method: {method}\n"
            f"\n"
        )

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_end_step(cls, url: str, method: str):

        data_to_add = (
            f"End time: {str(datetime.datetime.now())}\n"
            f"End name method: {method}\n"
            f"URL: {url}\n"
            f"\n-----\n"
        )

        cls.write_log_to_file(data_to_add)
