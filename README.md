# German_SQUADv2.0

## Motivation
Most of the data for Q/A are in English. To my knowledge, there is for German currently only one open-source Q/A dataset from Facebook ([MLQA dataset](https://github.com/facebookresearch/MLQA)). Creating questions and answers is a time consuming process which cannot be done by a single person in a reasonable amount of time. 
In order to gain more data, I deciced to use the current state of the art transformer T5 from Huggingface. T5 has already a "built-in" capability to translate text easily from Englisch to German.

If you do not want to use the T5 you can use another transformer for translating the data into to language of your choice


## Modifications of SQUAD v2 dataset:
- Translated into German using T5 from Huggingface
- adapted start_answer to context (in translated data)
- if translated (plausible) answers cannot be found in translated context, these answers will be dropped
- Contexts to which no (plausible) answers are left, were dropped

## Procedure
1. (Optional) Split Squad-Dataset into smaller chunks
In case you need to smaller chunks (especially of the SQUADv2-Train dataset) you can apply this script `split_squad.py`
2. Run `translate_t5_squad.py` in order to translate dataset into German
You may run this script on a Juypter Notebook (e.g. Colab) in order to use GPU-Support. All answers, plausible answers and contexts will be translated into German
3. Adjust start of answers in translated texts
Once all the texts, anwers and contexts were translated you need to adjust the start of the answers to the (translated) German context. Additionally, delete answers that cannot be found in context. Furthermore, delete answers that contain only "" as String. For this run `adjust_answers_start.py`.
4. (Optional) Merge datasets into one (training)-file
Apply this script `Merge_translated_squad_files.py` if you performed Step 1
5. Remove question and answers that contain no answers
Remove qas that contain no `answers`. Additionally, if there are paragraphs containing no answers at all, remove this parapragh. Use the script `clean_processed_files.py`

## Helper scripts
- `print_squad_items.py`: pretty prints the content ot a dataset in SQUADv2 format
- `utils.py`: contains functions for loading and dumping json files



## License: 
SQUAD v2 von CC BY-SA 4.0
Citation 
```
@article{Rajpurkar_2018,
   title={Know What You Don’t Know: Unanswerable Questions for SQuAD},
   url={http://dx.doi.org/10.18653/v1/P18-2124},
   DOI={10.18653/v1/p18-2124},
   journal={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
   publisher={Association for Computational Linguistics},
   author={Rajpurkar, Pranav and Jia, Robin and Liang, Percy},
   year={2018}
}
```