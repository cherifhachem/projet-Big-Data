@echo off

call conda activate projet-stockage

set JAVA_HOME=C:\Program Files\Eclipse Adoptium\jdk-17.0.19.10-hotspot

set HADOOP_HOME=C:\hadoop

set PATH=%PATH%;C:\hadoop\bin

set PYSPARK_PYTHON=python
set PYSPARK_DRIVER_PYTHON=python


python main.py

pause