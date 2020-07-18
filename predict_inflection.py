import torch, os

 sys.path.insert(0, './src')

 fpath = 'checkpoints/sigmorphon20-task0/mono-hmm/default/eng.nll_0.0071.acc_96.4858.dist_0.0814.epoch_14'

 my_model = torch.load(fpath)

#  my_model
#  MonoTagHMMTransducer(
#   (src_embed): Embedding(77, 200, padding_idx=0)
#   (trg_embed): Embedding(77, 200, padding_idx=0)
#   (enc_rnn): LSTM(200, 400, num_layers=2, dropout=0.4, bidirectional=True)
#   (dec_rnn): StackedLSTM(
#     (layers): ModuleList(
#       (0): LSTMCell(240, 400)
#     )
#     (dropout): Dropout(p=0.4, inplace=False)
#   )
#   (scale_enc_hs): Linear(in_features=800, out_features=400, bias=True)
#   (linear_out): Linear(in_features=1200, out_features=1200, bias=True)
#   (final_out): Linear(in_features=1200, out_features=77, bias=True)
#   (dropout): Dropout(p=0.4, inplace=False)
#   (attr_embed): Embedding(9, 40, padding_idx=0)
#   (merge_attr): Linear(in_features=320, out_features=40, bias=True)
# )
