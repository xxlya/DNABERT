cd examples

export KMER=6
export MODEL_PATH=6-new-12w-0
export DATA_PATH=sample_data/deepsea/$KMER
export OUTPUT_PATH=./ft/deepsea/$KMER

python run_finetune.py \
    --model_type deepsea \
    --tokenizer_name=dna$KMER \
    --model_name_or_path $MODEL_PATH \
    --task_name deepsea \
    --do_train \
    --do_eval \
    --data_dir $DATA_PATH \
    --max_seq_length 335 \
    --per_gpu_eval_batch_size=16   \
    --per_gpu_train_batch_size=16   \
    --learning_rate 2e-4 \
    --num_train_epochs 3.0 \
    --output_dir $OUTPUT_PATH \
    --evaluate_during_training \
    --logging_steps 100 \
    --save_steps 4000 \
    --warmup_percent 0.1 \
    --hidden_dropout_prob 0.1 \
    --overwrite_output \
    --weight_decay 0.01 \
    --n_process 1

