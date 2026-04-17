# [x] install libs - pip install -r requirements.txt:

from util import *

# [x] Directory path
directory  = os.path.dirname(os.path.abspath(__file__))
# [x] Buid datapath -> dataset base
file_path = os.path.join(directory, '..', 'DATASET', 'bootcamp_train.csv')
# [x] Loading pandas DataFrame
df_dataset = pd.read_csv(file_path)

df_train = df_dataset.copy(deep=True)

# > Debugger 
sys.stdout.write(df_train.head())

sys.stdout.write(df_train.info())

sys.stdout.write(df_train['falha_maquina'].value_counts())
# -------

# TO-DO
# [ ] Classe analysis

df_train['falha_maquina'] = df_train['falha_maquina'].str.lower()

df_train['falha_maquina'] = df_train['falha_maquina'].replace(['não', 'n', '0'], 'sem_falha')

df_train['falha_maquina'] = df_train['falha_maquina'].replace(['sim', 'y', '1'], 'com_falha')

# > Debugger 
sys.stdout.write(df_train['falha_maquina'].value_counts())

sys.stdout.write(df_train['FDF (Falha Desgaste Ferramenta)'].value_counts())
# ------

df_train['FDF (Falha Desgaste Ferramenta)'] = df_train['FDF (Falha Desgaste Ferramenta)'].replace(['False', 'N', '0', '-'], 0)


df_train['FDF (Falha Desgaste Ferramenta)'] = df_train['FDF (Falha Desgaste Ferramenta)'].replace(['True', '1'], 1)

# > Debugger 
sys.stdout.write(df_train['FDF (Falha Desgaste Ferramenta)'].value_counts())

sys.stdout.write(df_train['FDC (Falha Dissipacao Calor)'].value_counts())
# ----------

df_train['FDC (Falha Dissipacao Calor)'] = df_train['FDC (Falha Dissipacao Calor)'].replace(['False', 'nao', '0'], 0)

df_train['FDC (Falha Dissipacao Calor)'] = df_train['FDC (Falha Dissipacao Calor)'].replace(['True', 'y', '1'], 1)

# > Debugger 
sys.stdout.write(df_train['FDC (Falha Dissipacao Calor)'].value_counts())
sys.stdout.write(df_train['FP (Falha Potencia)'].value_counts())

# --------------

# 'sem falha' para 0
df_train['FP (Falha Potencia)'] = df_train['FP (Falha Potencia)'].replace(['False', 'N', '0'], 0)

#'com falha' para 1
df_train['FP (Falha Potencia)'] = df_train['FP (Falha Potencia)'].replace(['True', '1'], 1)

# > Debugger <<<
sys.stdout.write(df_train['FA (Falha Aleatoria)'].value_counts())
#-------------------

# 'sem falha' para 0
df_train['FA (Falha Aleatoria)'] = df_train['FA (Falha Aleatoria)'].replace(['Não', 'não', '0', '-'], 0)

# 'com falha' para 1
df_train['FA (Falha Aleatoria)'] = df_train['FA (Falha Aleatoria)'].replace(['Sim', 'sim', '1'], 1)

# > Debugger
sys.stdout.write(df_train['FA (Falha Aleatoria)'].value_counts())
sys.stdout.write(df_train.describe())
# ------------------

# Unificando os valores que indicam 'sem falha' para 0
df_train['FA (Falha Aleatoria)'] = df['FA (Falha Aleatoria)'].replace(['Não', 'não', '0', '-'], 0)

# Unificando os valores que indicam 'com falha' para 1
df_train['FA (Falha Aleatoria)'] = df['FA (Falha Aleatoria)'].replace(['Sim', 'sim', '1'], 1)

# > Debugger
sys.stdout.write(df_train['FA (Falha Aleatoria)'].value_counts())
#-------------

# Numeric Column 
# [ ] Loading class
nan_numerics_columns = ['temperatura_ar', 'temperatura_processo', 'velocidade_rotacional', 'torque', 'desgaste_da_ferramenta']

for column in nan_numerics_columns:
    df_train[column].fillna(df_train[column].median(), inplace = True)

# > Debugger
sys.stdout.write(df_train.info())
# ---------------

# Valores faltantes -> mediana
for column in nan_numerics_columns:
    df_train[column] = df_train[column].fillna(df_train[column].median())

# Análise de valores nulos
# Debugger
sys.stdout.write(df_train.info())

sys.stdout.write(df_train['tipo'].value_counts())
#-------------

tipo_dummies = pd.get_dummies(df_train['tipo'], prefix='tipo')

df_train = pd.concat([df_train, tipo_dummies], axis = 1)

df_train = df_train.drop('tipo', axis = 1)

# Debugger 
sys.stdout.write(df_train.head())
sys.stdout.write(df_train['id_produto'].value_counts())
# --------

df_train = df_train.drop('id_produto', axis=1)

# Debugger
sys.stdout.write(df_train.info())
#--------------------------------

df_train = df_train.drop(['id'], axis=1)

df_train['falha_maquina'] = df_train['falha_maquina'].replace(['sem_falha', 'com_falha'], [0, 1])

# Imprime a contagem de valores para verificar a mudança
sys.stdout.write(df_train['falha_maquina'].value_counts())

# Separa as variáveis preditoras (X) e a variável-alvo (y)
X = df_train.drop('falha_maquina', axis=1)
y = df_train['falha_maquina']

# Debugger
# Imprimindo o formato (shape) dos novos DataFrames para verificação
sys.stdout.write("Formato de X:", X.shape)
sys.stdout.write("Formato de y:", y.shape)

sys.stdout.write(X.info())
# -------------------------------------------------------------------

# Unificando os valores que indicam 'sem falha' para 0
df_train['FP (Falha Potencia)'] = df_train['FP (Falha Potencia)'].replace(['Não', 'não', 'N', '0'], 0)

# Unificando os valores que indicam 'com falha' para 1
df_train['FP (Falha Potencia)'] = df_train['FP (Falha Potencia)'].replace(['Sim', 'sim', '1', 'y'], 1)

# Debugger
# Imprimindo a contagem de valores para verificar a mudança
sys.stdout.write(df_train['FP (Falha Potencia)'].value_counts())

sys.stdout.write(df_train['FP (Falha Potencia)'].value_counts())
# ----------------------------------------------------------------------------------------------------------------

# MODELING ------------------------------------------------------------------------------------------------------
# -> random_state range or random 
# Seed analysis
seed_analysis = random.seed()

# Converte o y para o formato numérico
y = y.astype(int)

# Divisão treino/teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size = 0.2, random_state = seed_analysis)

# SMOTE (Synthetic Minority Over-sampling Technique): balancear os dados de treine
smote = SMOTE(random_state = seed_analysis) 
X_treino_smote, y_treino_smote = smote.fit_resample(X_treino, y_treino)

# Verificando a nova contagem de classes após o SMOTE
sys.stdout.write("Contagem de classes antes do SMOTE:", y_treino.value_counts())
sys.stdout.write("Contagem de classes após o SMOTE:", y_treino_smote.value_counts())

# Criando e treinando o modelo com os dados balanceados
modelo = DecisionTreeClassifier(random_state = seed_analysis)
modelo.fit(X_treino_smote, y_treino_smote)

# Previsões
y_predicao = modelo.predict(X_teste)

# Debuggger
# Avaliação
sys.stdout.write("Acuracia do modelo:", accuracy_score(y_teste, y_predicao))
sys.stdout.write("\nRelatorio de Classificacao:")
sys.stdout.write(classification_report(y_teste, y_predicao))
# ----------------------------

# CHARTS ------------------------------------------------------------------------------------------
# [ ] Type analysis
# [ ] Multiplot documentation 

x,y = 25, 15

tipo_counts = df_train[['tipo_L', 'tipo_M', 'tipo_H']].sum()

# Define o tamanho geral da figura
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(x, y))
fig.suptitle('Análise Exploratória e Avaliação do Modelo para Predição de Falhas', fontsize=20)

# Gráfico 1: Histograma (Posição 0, 0)
axes[0, 0].hist(df_train['temperatura_ar'], bins=20, color='skyblue', edgecolor = 'black')
axes[0, 0].set_title('1 - Distribuição da Temperatura do Ar', fontsize = 14)
axes[0, 0].set_xlabel('Temperatura do Ar (°C)')
axes[0, 0].set_ylabel('Frequência')
axes[0, 0].grid(axis = 'y', alpha = 0.75)

# Gráfico 2: Gráfico de Barras (Posição 0, 1)
tipo_counts.plot(kind = 'bar', ax = axes[0, 1], color=['skyblue', 'salmon', 'lightgreen'])
axes[0, 1].set_title('2 - Contagem de Máquinas por Tipo', fontsize=14)
axes[0, 1].set_xlabel('Tipo de Máquina')
axes[0, 1].set_ylabel('Contagem')
axes[0, 1].tick_params(axis='x', rotation=0)

# Gráfico 3: Matriz de Confusão (Posição 1, 0)
sns.heatmap(confusion_matrix(y_teste, y_predicao), annot=True, fmt='d', cmap='Blues', ax = axes[1, 0],
            xticklabels=['Predito: Sem Falha', 'Predito: Com Falha'], 
            yticklabels=['Real: Sem Falha', 'Real: Com Falha'])
axes[1, 0].set_title('3 - Matriz de Confusão', fontsize = 14)
axes[1, 0].set_xlabel('Valor Predito')
axes[1, 0].set_ylabel('Valor Real')

importances = modelo.feature_importances_
feature_names = X_treino.columns
indices = np.argsort(importances)[::-1]

sns.barplot(x=importances[indices], y=feature_names[indices], ax=axes[1, 1], palette='viridis')
axes[1, 1].set_title('4 - Main Features', fontsize = 14)
axes[1, 1].set_xlabel('Importância Relativa')
axes[1, 1].set_ylabel('Features')

# Ajusta o layout para evitar sobreposição de títulos e eixos
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Mostra a figura com todos os gráficos
plt.show()