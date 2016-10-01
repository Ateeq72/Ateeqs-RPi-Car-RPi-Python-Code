import motorController as mc
import pirController as pc

import cherrypy
import os

class Root:
    @cherrypy.expose
    def index(self):
        page = """
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Ateeq's Joystick</title>
                <meta name="viewport" content="width=device-width, initial-scale=0.5, maximum-scale=0.5">
                <style>
                    html, body {
                        position: absolute;
                        top: 0;
                        left: 0;
                        right: 0;
                        bottom: 0;
                        padding: 0;
                        margin: 0;
                    }
                    #left {
                        position: absolute;
                        left: 0;
                        top: 0;
                        height: 100%;
                        width: 50%;
                        background: rgba(0, 255, 0, 0.1);
                    }
                    #right {
                        position: absolute;
                        right: 0;
                        top: 0;
                        height: 100%;
                        width: 50%;
                        background: rgba(0, 0, 255, 0.1);
                    }
                    #debugR {
                        position: absolute;
                        right: 0;
                        top: 0;
                        height: 100%;
                        width: 50%;
                        background: rgba(0, 0, 255, 0.1);
                    }
                    #debugL {
                        position: absolute;
                        right: 0;
                        top: 0;
                        height: 100%;
                        width: 50%;
                        background: rgba(0, 0, 255, 0.1);
                    }
                </style>
            </head>
            <body>
            <div id="left"></div>
            <div id="right"></div>
            <script src="./node_modules/nipplejs/dist/nipplejs.js"></script>
            <script src="./node_modules/jquery/dist/jquery.js"></script>
            <script>
                var joystickL = nipplejs.create({
                    zone: document.getElementById('left'),
                    mode: 'dynamic',
                    position: { left: '20%', top: '50%' },
                    color: 'green',
                    size: 200
                });
                console.log(joystickL);
                var joystickR = nipplejs.create({
                    zone: document.getElementById('right'),
                    mode: 'dynamic',
                    position: { left: '80%', top: '50%' },
                    color: 'red',
                    size: 200
                });
                console.log(joystickR);
                function bindNippleL () {
                    joystickL.on('start end', function (evt, data) {
                        var dataToSend = {};
                        dataToSend['action'] = evt.type;
                        jQuery.post('/doStuffHandler',dataToSend);
                        //console.log(data);
                    }).on('move', function (evt, data) {
                        //console.log(data);
                    }).on('dir:up dir:down ',
                            function (evt, data) {
                                var dataToSend = {};
                                dataToSend['action'] = data.direction.y;
                                jQuery.post('/doStuffHandler',dataToSend);
                                console.log('LJS : '+evt.type);
                            }
                    ).on('pressure', function (evt, data) {
                        //console.log(data);
                    });
                }
                function bindNippleR () {
                    joystickR.on('start end', function (evt, data) {
                        var dataToSend = {};
                        dataToSend['action'] = evt.type;
                        jQuery.post('/doStuffHandler',dataToSend);
                       // console.log(data);
                    }).on('move', function (evt, data) {
                       // console.log(data);
                    }).on('dir:left dir:right',
                            function (evt, data) {
                                var dataToSend = {};
                                dataToSend['action'] = data.direction.x;
                               jQuery.post('/doStuffHandler',dataToSend);
                                console.log('RJS : '+evt.type);
                            }
                    ).on('pressure', function (evt, data) {
                        //console.log(data);
                    });
                }
                bindNippleL();
                bindNippleR();
            </script>
            </body>
             <html>
            """
        return page

    @cherrypy.expose
    def doStuffHandler(self, **data):
        dataRec = data['action']
        mc.initialSetup()
        if(pc.checkObs()):
            os.system("echo 'Obstacle Detected!' | festival --tts ")
            exit
        if (dataRec != ""):
            if(dataRec == "dir:up"):
                mc.forward()
            elif(dataRec == "dir:down"):
                mc.backword()
            elif(dataRec == "dir:right"):
                mc.turnRight()
            elif(dataRec == "dir:left"):
                mc.turnLeft()
            #elif(dataRec == "start"):
            #    os.system("espeak 'Started!'")
            #elif(dataRec == "end"):
            #    os.system("espeak 'Ended!'")
            else:
                mc.done()




conf = os.path.join(os.path.dirname(__file__), 'cherrypy.conf')
if __name__ == '__main__':
    root = Root()
    cherrypy.quickstart(root, config=conf)