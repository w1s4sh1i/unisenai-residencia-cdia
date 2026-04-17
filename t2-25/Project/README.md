# UniSenai - RT 2/25 [Project]

Residência em Ciência de Dados e Inteligência Artificial pela [UniSenai - Edital 2025 / 2](https://sites.google.com/edu.sc.senai.br/residencia-ia/)

# Description

O objetivo do projeto é desenvolver um sistema inteligente de manutenção preditiva. Desenvolver um modelo de classificação multiclasse para prever os 5 tipos de defeitos a partir de 8 atributos de sensores IoT. Para cada nova medição, o sistema retornará a falha prevista e sua probabilidade. A empresa também receberá um relatório com insights e visualizações sobre as causas dos defeitos e a importância de cada sensor, agregando valor estratégico à operação.

O plano de ação começa com uma análise exploratória para gerar os insights visuais. Em seguida, treinar e avaliar os modelos de classificação, como SMOTE, "Random Forest" ou caracterização por SVMs, ao usar métricas de performance e matriz de confusão para garantir a precisão. Por fim, o modelo com melhor desempenho será "empacotado" em um protótipo funcional, com objetivo de integrado e ser utiliza pela equipe de manutenção da uma empresa target.

# Requirements
```
$ pip install -r requirements.txt
```

# Organization
```
unisenai-residencia-cdia-t225/
├── README.md
├── requirements.txt
├── DATASET
|   ├── bootcamp_train.py
|   └── bootcamp_test.py
└── SOURCE
    ├── demonstration.py
    ├── failure_prediction.py
    └── util.py
    └── __init__.py
```

# References

1. [Predicting Failure Probability in Industry 4.0 Production Systems: A Workload-Based Prognostic Model for Maintenance Planning](https://www.mdpi.com/2076-3417/13/3/1938);

2. [A Systematic Literature Review on Applying CRISP-DM Process Model](https://www.sciencedirect.com/science/article/pii/S1877050921002416);

3. [SMOTE: Synthetic Minority Over-sampling Technique](https://arxiv.org/abs/1106.1813);

4. [A Primer for tinyML Predictive Maintenance: Input and Model Optimisation](https://backend.orbit.dtu.dk/ws/portalfiles/portal/274322308/A_Primer_for_tinyML_Predictive_Maintenance_Input_and_Model_Optimisation.pdf);

5. [Internet of things for smart factories in industry 4.0, a review](https://www.sciencedirect.com/science/article/pii/S2667345223000275);
