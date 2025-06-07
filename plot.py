import matplotlib.pyplot as plt 
import numpy as numpy
import pandas as pd 



speaker0_df = pd.read_csv('aihub_0.csv')
speaker0_upscale_df = pd.read_csv('aihub_upscale_0.csv')
speaker1_df = pd.read_csv('aihub.csv')

plt.title("SIGNAL SCORES")
plt.plot(speaker0_df['SIG'], label="Speaker 0")
plt.plot(speaker0_upscale_df['SIG'], label="Speaker 0 upscaled")
plt.plot(speaker1_df['SIG'], label="Speaker 1")
plt.legend()
plt.savefig("result.png")
plt.clf()




