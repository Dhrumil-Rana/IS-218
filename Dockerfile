FROM python:3.7

ADD . .

Run pip install -r requirements.txt

CMD [ "python", "./Test/CalculatorTest.py" ]