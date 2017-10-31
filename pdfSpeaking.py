import pyttsx


def fileSpeaker(file):

    speaker = pyttsx.init()
    speaker.setProperty('rate',150)
    speaker.setProperty('voice','en+m7')
    speaker.say(file)
    speaker.runAndWait()

