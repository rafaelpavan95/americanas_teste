FROM python:3.8-slim-buster

RUN mkdir -p /home/notebooks

WORKDIR /home/notebooks


# packages

RUN pip install --upgrade pip

RUN pip install numpy

RUN pip install pandas

RUN pip install notebook

RUN pip install pandas pyarrow

RUN pip install scikit-learn

RUN pip install xgboost

RUN pip install seaborn

RUN pip install matplotlib

RUN pip install scipy

# container port
		
EXPOSE 8888

ENTRYPOINT ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser"]

# sudo docker build -t americanas .



