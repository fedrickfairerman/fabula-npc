import customtkinter as ctk

# --- CONFIGURAÇÃO GLOBAL ---
# Define o tema escuro (dark) ou claro (light)
ctk.set_appearance_mode("dark") 
# Define a paleta de cores principal dos botões e seletores
ctk.set_default_color_theme("blue") 

# Criamos uma "Classe". Pense nela como a Planta Arquitetônica do seu App.
class AppFabula(ctk.CTk):
    def __init__(self):
        super().__init__() # Inicializa a janela base do CustomTkinter

        # Título da janela e tamanho inicial (Largura x Altura)
        self.title("Fábula Ultima - Criador de NPCs")
        self.geometry("650x850")

        # --- CABEÇALHO ---
        # CTkLabel é usado para textos simples (etiquetas)
        self.lbl_titulo = ctk.CTkLabel(self, text="GERADOR DE NPC", font=("Roboto", 26, "bold"))
        # .pack() é o comando que "coloca" o objeto na tela. 
        # pady=20 adiciona um espaçamento em cima e embaixo.
        self.lbl_titulo.pack(pady=20)

        # --- ÁREA DE ROLAGEM (ScrollableFrame) ---
        # Criamos um container que permite rolar a tela se o conteúdo for grande
        self.main_frame = ctk.CTkScrollableFrame(self, width=600, height=700)
        self.main_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # --- SELEÇÃO DE CATEGORIA (OptionMenu) ---
        self.lbl_cat = ctk.CTkLabel(self.main_frame, text="1. Escolha a Categoria do NPC:", font=("Roboto", 16, "bold"))
        self.lbl_cat.pack(pady=(10, 5), anchor="w") # anchor="w" alinha o texto à esquerda (West)
        
        # StringVar é uma variável especial que guarda o texto selecionado no menu
        self.cat_var = ctk.StringVar(value="Soldado")
        self.menu_categoria = ctk.CTkOptionMenu(self.main_frame, 
                                                values=["Soldado", "Elite", "Campeão"],
                                                variable=self.cat_var)
        self.menu_categoria.pack(fill="x", padx=20)

        # --- SEÇÃO DE ATRIBUTOS ---
        self.lbl_attrs = ctk.CTkLabel(self.main_frame, text="2. Defina os Atributos:", font=("Roboto", 16, "bold"))
        self.lbl_attrs.pack(pady=(20, 5), anchor="w")

        # Criamos um Frame interno apenas para organizar as caixinhas de atributos
        self.attr_frame = ctk.CTkFrame(self.main_frame)
        self.attr_frame.pack(fill="x", padx=10, pady=5)

        # Aqui usamos a função auxiliar 'criar_campo_attr' que definimos lá embaixo
        self.ent_nivel = self.criar_campo_attr(self.attr_frame, "Nível do NPC:", "5")
        self.ent_dex = self.criar_campo_attr(self.attr_frame, "Dexterity (DEX):", "8")
        self.ent_ins = self.criar_campo_attr(self.attr_frame, "Insight (INS):", "8")
        self.ent_mig = self.criar_campo_attr(self.attr_frame, "Might (MIG):", "8")
        self.ent_wlp = self.criar_campo_attr(self.attr_frame, "Willpower (WLP):", "8")

        # --- SELEÇÃO DE TIPO ---
        self.lbl_tipo = ctk.CTkLabel(self.main_frame, text="3. Escolha o Tipo de Criatura:", font=("Roboto", 16, "bold"))
        self.lbl_tipo.pack(pady=(20, 5), anchor="w")

        self.tipo_var = ctk.StringVar(value="Humanoide")
        self.menu_tipo = ctk.CTkOptionMenu(self.main_frame, 
                                          values=["Humanoide", "Monstro", "Constructo", "Demonio", "Fera", "Elemental", "Planta", "Undead"],
                                          variable=self.tipo_var)
        self.menu_tipo.pack(fill="x", padx=20)

        # --- BOTÃO GERAR ---
        # command=self.processar_npc diz ao botão qual função executar ao ser clicado
        self.btn_gerar = ctk.CTkButton(self.main_frame, text="GERAR FICHA FINAL", 
                                       font=("Roboto", 18, "bold"),
                                       height=50,
                                       fg_color="#2c6e49", # Cor verde floresta
                                       hover_color="#1e4a32", # Verde mais escuro ao passar o mouse
                                       command=self.processar_npc)
        self.btn_gerar.pack(pady=30, padx=20, fill="x")

        # --- ÁREA DE RESULTADO (Onde a ficha aparece) ---
        self.res_frame = ctk.CTkFrame(self.main_frame, fg_color="#1a1a1a", border_width=2, border_color="#333333")
        self.res_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.txt_resultado = ctk.CTkLabel(self.res_frame, text="Aguardando dados...", 
                                          font=("Consolas", 15), # Fonte Consolas é ótima para fichas (monaçapa)
                                          justify="left")
        self.txt_resultado.pack(pady=20, padx=20)

    # --- FUNÇÃO AUXILIAR DE INTERFACE ---
    def criar_campo_attr(self, parent, label_text, default_val):
        """ Cria uma linha com um texto e uma caixa de entrada (Entry) ao lado """
        row = ctk.CTkFrame(parent, fg_color="transparent")
        row.pack(fill="x", pady=2, padx=10)
        
        lbl = ctk.CTkLabel(row, text=label_text, width=150, anchor="w")
        lbl.pack(side="left") # Alinha o texto à esquerda da linha
        
        ent = ctk.CTkEntry(row, width=80)
        ent.insert(0, default_val) # Coloca o valor padrão na caixa
        ent.pack(side="right") # Alinha a caixa à direita da linha
        return ent

    # --- FUNÇÃO DE LÓGICA (O MOTOR DO APP) ---
    def processar_npc(self):
        """ Coleta os dados da interface e aplica as regras de Fabula Ultima """
        imu, vul, resist, cond_imu = [], [], [], []
        
        try:
            # .get() busca o que o usuário digitou ou selecionou na tela
            nivel = int(self.ent_nivel.get())
            dex = int(self.ent_dex.get())
            ins = int(self.ent_ins.get())
            mig = int(self.ent_mig.get())
            wlp = int(self.ent_wlp.get())
            categoria = self.cat_var.get()
            tipo_criatura = self.tipo_var.get()

            # Aqui aplicamos a matemática que você já criou (simplificada para o exemplo)
            # HP, MP, Iniciativa, Skills...
            mp_base = (nivel + (ins * 5))
            if categoria == "Soldado":
                vida = (nivel * 2) + (mig * 5)
                mp = mp_base
            elif categoria == "Elite":
                vida = ((nivel * 2) + (mig * 5)) * 2
                mp = mp_base
            else: # Campeão
                vida = ((nivel * 2) + (mig * 5)) * 2
                mp = mp_base * 2

            # ... (Restante da sua lógica de Undead, Fera, etc) ...
            if tipo_criatura == "Undead":
                imu.extend(["Dark", "Poison"])
                vul.append("Light")

            # ATUALIZAÇÃO DA INTERFACE:
            # .configure(text=...) muda o texto da etiqueta na tela em tempo real
            ficha = f"HP: {vida} | MP: {mp}\nTipo: {tipo_criatura}\nImunidades: {imu}"
            self.txt_resultado.configure(text=ficha)

        except ValueError:
            # Caso o usuário digite letras onde deveriam ser números
            self.txt_resultado.configure(text="ERRO: Use apenas números nos atributos!")

# --- INICIALIZAÇÃO ---
if __name__ == "__main__":
    app = AppFabula()
    app.mainloop() # Mantém a janela aberta rodando