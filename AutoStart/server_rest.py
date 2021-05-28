from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
#import RPi.GPIO as GPIO
import pigpio

app = Flask(__name__)
api = Api(app)
CORS(app)

pi = pigpio.pi()


#FREQ = 50  #Frequency for PWM [Hz]
#PIN = 37
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(PIN, GPIO.OUT)
#pwm = GPIO.PWM(PIN, FREQ)
#pwm.start(0)

setValue = 0

class HelloWorld(Resource):
    def get(self):
        global setValue
        return setValue, 200

    def post(self):
        global setValue
        return self.put()

    def put(self):
        global setValue
        parser = reqparse.RequestParser()
        parser.add_argument("val", type=float, help="val is not a float");
        args = parser.parse_args()
        for k,v in args.items():
            if v is not None:
                #Value set
                setValue = v
                #pwm.ChangeDutyCycle(setValue)
                pi.hardware_PWM(18,5000,int(setValue*10000))
        return setValue, 200

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host= '0.0.0.0', port=5000)
