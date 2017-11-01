import random
import webbrowser

history_record = open("history.txt","a+")


HTTP_URL="http://"

USER_INFO_QUESTION = False

GREETING_KEYWORDS = ("hello", "hi", "greetings", "what's up")
GREETING_RESPONSES = ["Hello", "Hi", "Greetings"]
CONFIRMATION = ["yes","yup","yap","of course","ofcourse","afirmitive","agreed"]
NEGATION = ["no","stop","don't","dont"]
NEGATION_RESPONSES = ["ok, we wont talk about it", "np, just chill"]
BASIC_QUESTIONS = []
MAKER_QUESTIONS = ["who made you?", "who is your maker?"]
MAKER_RESPONSES=["One guy"]
FUNNY_MAKER_QUESTIONS = ["who is your father?", "who is your daddy?"]
FUNNY_MAKER_RESPONSE =["Luke, I am your father!"]
FELLING_QUESTIONS = []
TIME_QUESTIONS = []
ERROR_RESPONSES =["sry, didnt cath that?", "i dont understand you."]
