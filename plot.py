import matplotlib.pyplot as plt 
import numpy as numpy
import pandas as pd 


# speaker0_df = pd.read_csv('aihub_0.csv')
# speaker0_upscale_df = pd.read_csv('aihub_upscale_0.csv')
# speaker1_df = pd.read_csv('aihub.csv')
# 
# plt.title("SIGNAL SCORES")
# plt.plot(speaker0_df['SIG'], label="Speaker 0")
# plt.plot(speaker0_upscale_df['SIG'], label="Speaker 0 upscaled")
# plt.plot(speaker1_df['SIG'], label="Speaker 1")
# plt.legend()
# plt.savefig(f"result_sig.png")
# plt.clf()
# 
# plt.title("BACKGROUND SCORES")
# plt.plot(speaker0_df['BAK'], label="Speaker 0")
# plt.plot(speaker0_upscale_df['BAK'], label="Speaker 0 upscaled")
# plt.plot(speaker1_df['BAK'], label="Speaker 1")
# plt.legend()
# plt.savefig(f"result_bak.png")
# plt.clf()

data = pd.read_csv("middle1.csv")
plt.title("SIGNAL SCORES")
plt.plot(data['SIG'], label="Speaker 0")
plt.legend()
plt.savefig(f"result_sig.png")
plt.clf()

plt.title("BACKGROUND SCORES")
plt.plot(data['BAK'], label="Speaker 0")
plt.legend()
plt.savefig(f"result_bak.png")
plt.clf()

# data = pd.read_csv('experiment.csv')
# 
# data_quiet = data.loc[data['filename'].str.contains('quiet')]
# data_noisy = data.loc[data['filename'].str.contains('noisy')]
# data_noisy.index = range(len(data_noisy))
# plt.title("SIGNAL SCORES")
# plt.plot(data_quiet['SIG'], label="Quiet")
# plt.plot(data_noisy['SIG'], label="Noisy")
# plt.legend()
# plt.savefig(f"result_sig.png")
# plt.clf()
# 
# plt.title("BACKGROUND SCORES")
# plt.plot(data_quiet['BAK'], label="Quiet")
# plt.plot(data_noisy['BAK'], label="Noisy")
# plt.legend()
# plt.savefig(f"result_bak.png")
# plt.clf()

