import os
from subprocess import call

# Set the path to your mallet package (make sure to change the mallet version number, if necessary)
# Create directory "inputdirectory" within this mallet directory. Load the files to be analyzed in "inputdirectory"
mallet_path = "./mallet-2.0.8RC3"
input_path = "./wikimedia_russian_texts/txt/"

# Specify the number of topics you wish to obtain, and tbe number of iterations you wish to use
# to obtain those topics. Store both values as string (keep the numbers in quotation marks, or use str() method below)
# Caveat lector: Running 30000 iterations takes a few minutes...
num_topics = "100"
num_iterations = "1000"

# One could add additional parameters here (e.g. --optimize-interval could be helpful)
class Mallet(object):
  def __init__(self, input_path, mallet_path):
    """Initialize the Mallet class parameters and user configurations"""
    self.mallet_exec = mallet_path + "/bin/mallet"
    self.output_dir  = mallet_path + "/topic_modelling_output/"

  def import_dir(self):
    """Call the first step for the topic modelling process""" 
    output = mallet_path + "/readyforinput.mallet"
    call(self.mallet_exec + " import-dir --input " + input_path + " --keep-sequence --output " + output , shell=True)

  def make_output_dir(self):
    """Create an output directory in which results may be stored"""
    if not os.path.exists(self.output_dir):
      os.makedirs(self.output_dir)
  
  def train_topics(self):
    """Generate the topic modelling output"""
    input_file = mallet_path + "/readyforinput.mallet"
    output_doc_topics = self.output_dir + "/output_doc_topics.txt"
    output_topic_keys = self.output_dir + "/output_topic_keys.txt"
    output_state = self.output_dir + "/output_state.gz"
    command = self.mallet_exec + " train-topics --input " + input_file + " --num-topics " + num_topics + " --output-doc-topics " + output_doc_topics + " --output-topic-keys " + output_topic_keys + " --output-state " + output_state + " --num-iterations " + num_iterations
    call(command, shell=True)

callmallet = Mallet(input_path, mallet_path)
callmallet.make_output_dir()
callmallet.import_dir()
callmallet.train_topics()

# how to hardcode path: os.path.abspath("mydir/myfile.txt")