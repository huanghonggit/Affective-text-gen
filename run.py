from model import run_pplm_example, resultContainer, load_model
from flask_socketio import SocketIO, join_room, emit, send

# Knob =  0.8
# Affect = "joy"
# Topic = "legal"
# Prompt = "There was a"

def generate(prompt, topic, affect, knob):
    # emit('word', {"value": "Loading model..."}, broadcast=True)
    # load_model()
    knob/=10
    print("generate called\n", "Prompt: ", prompt, "topic: ", topic, "affect: ", affect, "knob: ", knob)
    if prompt == "Enter prefix" or prompt == "":
        return "", False
    emit('word', {"value": "Generating..."}, broadcast=True)
    result = run_pplm_example(
          affect_weight=1,  # it is the convergence rate of affect loss, don't change it :-p
          knob = knob, # 0-1, play with it as much as you want
          cond_text=prompt,
          num_samples=1,
          bag_of_words=topic,
          bag_of_words_affect=affect,
          length=500,
          stepsize=0.01,
          sample=True,
          num_iterations=3,
          window_length=5,
          gamma=1.5,
          gm_scale=0.95,
          kl_scale=0.01,
          verbosity='quiet'
      )
    print(result)
    return result, True

# generate("There was a", "legal", "fear", 70)
