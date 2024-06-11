import os


if __name__ == '__main__':
    env_variables = ' '.join([f"{k}='{v}'" for k, v in os.environ.items()])
    command = f'{env_variables} streamlit run home.py'
    print(command)
    os.system(command)