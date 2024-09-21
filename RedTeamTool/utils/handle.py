def error_handling_wrapper(func, *args):
    try:
        func(*args)
    except Exception as e:
        print(f"Error occurred: {e}")
        log_error(e)
        # Retry logic if necessary
    finally:
        clean_up()  # Ensure that the environment is clean after any failure

def log_error(error):
    with open('error_log.txt', 'a') as log_file:
        log_file.write(str(error) + '\n')

def clean_up():
    print("Cleaning up resources after error.")
