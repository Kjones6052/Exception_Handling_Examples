try:
    print("Server is running...")
    raise Exception("Unexpected error!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Performing cleanup operations....")
    print("Shutting down server gracefully.")