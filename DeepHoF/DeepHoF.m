function DeepHoF(SeqFile, OutputFile)
if exist([pwd,'/tmp'],'dir')
    cmd=['rm -rf ',pwd,'/tmp'];
    unix(cmd);
end
cmd=['mkdir ',pwd,'/tmp'];
unix(cmd);
%%--------------------split sequence---------------------%%%
disp('split sequence');
split_fasta(SeqFile);
%%--------------------sequence one-hot coding-----------------------------------
disp('coding the sequence');
create_onehot('tmp/');
%%--------------------predict------------------%%
disp('predicting the host of the given viral sequence');
predict('tmp/')
%%-------------------combine the score from splited sequences-----------%%
disp('combining the predictions');
cmd=['python ',pwd,'/combine_groups_predicts.py ',SeqFile];
unix(cmd);
%%-------------------calculate the pvalue of the predictions-------------%%
disp('calculating the pvalues');
cmd=['python ',pwd,'/for_pvalue/calculate_pvalue.py ', 'tmp/score.txt ', OutputFile];
unix(cmd);
%cmd=['rm -rf ',pwd,'/tmp'];
%unix(cmd);
disp(' ')
disp('Finished.')  
