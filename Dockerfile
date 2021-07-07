FROM python:3

ADD . .

Run pip install -r requirements.txt

CMD [ "python", "./src/Test/CalculatorTest.py" ]