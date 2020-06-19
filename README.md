# German_SQUADv2.0

License: 
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
- Übersetzungen mit T5 von huggingface
- vorgenommen Änerungen: 
  * Texte, Fragen und Antworten auf Deutsch maschinell übersetzt
  * start_answer, end_answer angepasst
  * Antworten, die nach der Übersetzungen nicht mehr regelbasiert zugeordnet werden konnten, werden aus dem Datensatz gelöscht
  * Text zu denen nach der Bearbeitung keine Fragen mehr vorhanden waren, wurden aus dem usprünglichem Datensatz gelöscht