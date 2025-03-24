import streamlit as st


st.set_page_config(
    page_title="Meu Portfólio",
    page_icon="Logo.png",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get help": "https://github.com/AdieLaine/Streamly",
        "Report a bug": "https://github.com/AdieLaine/Streamly",
        "About": """
            ## Streamly Streamlit Assistant
            ### Powered using GPT-4o-mini

            **GitHub**: https://github.com/AdieLaine/

            The AI Assistant named, Streamly, aims to provide the latest updates from Streamlit,
            generate code snippets for Streamlit widgets,
            and answer questions about Streamlit's latest features, issues, and more.
            Streamly has been trained on the latest Streamlit updates and documentation.
        """
    }
)


# Streamlit Title



def main():
    tab1, tab2, tab3 = st.tabs(["Sobre mim", "Formação e experiência", "Projetos"])

    with tab1:
        # Informações do portfólio
        nome = "Micael Santana Trevizan"
        titulo = "Engenheiro de Produção | Engenharia de Sistemas e Produtos | P&D | Ciência de Dados"
        descricao = "Profissional multidisciplinar, formado em Engenharia de Produção. Tem experiência em gestão de projetos, otimização de processos, análise de dados e desenvolvimento de modelos preditivos aplicados ao setor de Qualidade. Atuou no desenvolvimento de projetos multidisciplinares no setor de tecnologia: sites, aplicativos, jogos e sistemas. Atualmente, aprofunda seus conhecimentos em Engenharia de Sistemas e Produto por meio de mestrado no Instituto Federal de Educação, Ciência e Tecnologia da Bahia, onde atua como pesquisador."
        st.title(nome)
        st.subheader(titulo)
        st.write(descricao)

        st.markdown("---")

        habilidades = ["Desenvolvimento de software","Metodologias ágeis","Gestão de projetos","Análise de dados", "Levantamento de requisitos", "Modelagem de dados", "Relatórios de indicadores-chave de desempenho (KPI)","Linguagens de programação", "Mapeamento de processos", "Sistema de qualidade", "Inteligência artificial"]
        # Habilidades
        st.header(":toolbox: Habilidades")
        st.write(", ".join(habilidades))

        # Rodapé
        st.markdown("---")
        st.subheader("\U0001F4DE Contato")
        st.write("Email: micaeltrevizan@hotmail.com")
        st.write("Linkedin: https://www.linkedin.com/in/micael-trevizan-93b733157/")
        st.write("Telefone: 71 9 9160 - 6671")

    with tab3:
        st.header("Projetos")

        col1, col2, col3= st.columns(3)
        with st.container():
                with col1:
                    curso = st.subheader("Ferramenta de Gerenciamento de Projetos com IA")
                    inst = st.write(":office: Instituto Federal de Educação, Ciência e Tecnologia da Bahia :date: 2025")
                    st.image("/home/linuxlite/Área de Trabalho/Streamlit/mica.png", width=250)
                    st.caption("Este projeto implementa uma ferramenta Streamlit que utiliza o modelo de Inteligência Artificial Gemini para auxiliar na criação de planos de gerenciamento de projetos Hibridos, baseados na metodologia MICA (METHODOLOGY IDENTIFICATION AND CHOICE ANALYSIS), desenvolvida durante o meu Mestrado.")
                    inst = st.caption("Proprietário/ Desenvolvedor")
                    inst = st.caption("Ferramentas: Python, Google Cloud, Generative AI, Streamlit")
                    st.markdown("[Link para o projeto](https://github.com/Micaeltrevizan/REFERENCEMODEL.git)")

                with col2:
                    curso = st.subheader("Automatização da Análise dos Dados de Qualidade")
                    inst = st.write(":office: Ford Motor Company :date: 2024")
                    st.image("/home/linuxlite/Área de Trabalho/Streamlit/data_-sience.jpg", width=250)
                    st.caption("O projeto Predição, Modelagem e Automatização da Análise dos Dados de Reclamações de Segurança e Qualidade visa otimizar o processo de tratamento de reclamações, utilizando inteligência artificial para prever, modelar e automatizar a análise de dados.")
                    inst = st.caption("Função: Pesquisador, Analista de Dados")
                    inst = st.caption("Ferramentas: Python, QlikSense, Alteryx, Google Cloud, SQL, Machine learning, Trello")
                    st.markdown("[Link para o projeto](https://drive.google.com/file/d/1pFHBFmlF00q6hWTrFZ7CW8kuuWXXrQh-/view?usp=drive_link)")

                with col3:
                    curso = st.subheader("Análise de dados de Qualidade na Manufatura Veícular")
                    inst = st.write(":office: Ford Motor Company :date: 2023")
                    st.image("/home/linuxlite/Área de Trabalho/Streamlit/ford.png", width=250)
                    st.caption("Este estudo detalhado teve como objetivo principal analisar minuciosamente os indicadores de qualidade cruciais que impactam a manufatura de veículos na região da América do Norte. Através de uma abordagem multifacetada, o estudo não apenas coletou e processou dados extensivos, mas também se aprofundou na interpretação desses dados para identificar tendências, padrões e áreas de melhoria.")
                    inst = st.caption("Função: Pesquisador, Analista de Dados")
                    inst = st.caption("Ferramentas: Python, QlikSense, Alteryx, Google Cloud, SQL")
                    st.markdown("[Link para o projeto](https://drive.google.com/file/d/1JJx5fg6QaLb404z81Jmt9TbINhN054pg/view?usp=sharing)")

        st.markdown("---")
        col4, col5, col6= st.columns(3)
        with st.container():
                with col4:
                    curso = st.subheader("Ferramenta de ajuste de valor e custo do produto.")
                    inst = st.write(":office: Ford Motor Company :date: 2022")
                    st.image("/home/linuxlite/Área de Trabalho/Streamlit/124672.jpg", width=250)
                    st.caption("O objetivo desse projeto é desenvolver uma ferramenta, a base de inteligência artificial, que identifique as oportunidades de melhorias no produto com melhor impacto na percepção do consumidor. ")
                    inst = st.caption("Função: Pesquisador, Analista de Dados")
                    inst = st.caption("Ferramentas: Python, QlikSense, Alteryx, Google Cloud, SQL, Machine learning, Trello")
                    st.markdown("[Link para o projeto](https://drive.google.com/file/d/1BTzjepGYDu5S70VnymnMTWQA5hQxcyAy/view?usp=sharing)")

                with col5:
                    curso = st.subheader("Processamento de Linguagem Natural utilizando CNN e BERT")
                    inst = st.write(":office: Produção independente :date: 2022")
                    st.image("/home/linuxlite/Área de Trabalho/Streamlit/ai.jpg", width=250)
                    st.caption("O objetivo principal deste código é treinar um modelo de aprendizado profundo capaz de analisar e classificar a categoria dos textos. Ele utiliza uma combinação de representações de palavras BERT para capturar o contexto semântico e uma CNN para extrair padrões e características relevantes dos textos.")
                    inst = st.caption("Função: Proprietário/ Desenvolvedor")
                    inst = st.caption("Ferramentas: Python, Machine learning, Redes neurais, Google Colab")
                    st.markdown("[Link para o projeto](https://github.com/Micaeltrevizan/DCNN_Classification.git)")

                with col6:
                    curso = st.subheader("Aplicativo educativo gamificado para alunos e colaboradores.")
                    inst = st.write(":office: Senai CIMATEC :date: 2022")
                    st.image("/home/linuxlite/Área de Trabalho/Streamlit/cimatec.png", width=300)
                    st.caption("Projeto de desenvolvimento mobile objetivando criar uma ferramenta educassional de concientização sobre à utilização das instalações da instituição, por alunos e colaboradores no Senai CIMATEC.")
                    inst = st.caption("Função: Designer")
                    inst = st.caption("Ferramentas: Unity, Photoshop, Trello, C#, JavaScript, Java, Blender")
                    st.markdown("[Link para o projeto](https://drive.google.com/drive/folders/1rbfsrFlTYgorijxOlBB9K5s6uc8stUaE?usp=sharing)")




        st.markdown("---")
        col7, col8, col9 = st.columns(3)
        with st.container():
                with col7:
                    curso = st.subheader("Construção de Aplicativo como estratégia para ensino de Cálculo Diferencial e Integral.")
                    inst = st.write(":office: Centro Universitário Jorge Amado :date: 2021")
                    st.image("/home/linuxlite/Área de Trabalho/Streamlit/MAPA2.png", width=300)
                    st.caption("Aplicação com o objetivo de auxiliar na aprendizagem do componente Cálculo nos cursos de Engenharia, utilizando elementos de gamificação com o intuito de apresentar de forma natural as aplicações e funcionalidades do cálculo matemático.")
                    inst = st.caption("Função: Gestor, Designer")
                    inst = st.caption("Ferramentas: Unity, Photoshop, Trello, C#")
                    st.markdown("[Link para o projeto](https://drive.google.com/drive/folders/1Vn064lFtbuyUq_JjkB7tby4uGqTnU7MA?usp=sharing)")
                
                with col8:
                    curso = st.subheader("Construção de Website e Jogo digital de Aventuras e Vivências nos Parques Urbanos")
                    inst = st.write(":office: Centro Universitário Jorge Amado :date: 2020")
                    st.image("/home/linuxlite/Área de Trabalho/Streamlit/vp.png", width=300)
                    st.caption('Este projeto tem como meta utilizar a tecnologia da informação para promover o conhecimento em temas ambientais dos parques metropolitanos na cidade de Salvador, começando pelo Parque de Pituaçu. ')
                    inst = st.caption("Função: Gestor, Designer")
                    inst = st.caption("Ferramentas: Unity, Photoshop, Trello, C#, JavaScript, Java, Blender")
                    st.markdown("[Link para o projeto](https://drive.google.com/drive/folders/1e2vA-vQ0s-zhuSJzPKfmULqlxAkBnxaj?usp=sharing)")

                with col9:
                    curso = st.subheader("Criação de Jogo Mobile para Prevenção e Conscientização de Situações em Áreas de Risco.")
                    inst = st.write(":office: Centro Universitário Jorge Amado :date: 2019")
                    st.image("/home/linuxlite/Área de Trabalho/Streamlit/mc.webp", width=300)
                    st.caption("Jogo para mobile e desktop que visa auxiliar e conscientizar pessoas que vivem em áreas de riscos em Salvador. Projeto foi uma parceria entre a Unijorge e a defesa civil de Salvador(Codesal).")
                    inst = st.caption("Função: Gestor, Designer")
                    inst = st.caption("Ferramentas: Unity, Photoshop, Trello, C#, JavaScript, Java, Blender")
                    st.markdown("[Link para o projeto](https://play.google.com/store/apps/details?id=com.dngadelha.MinhaComunidade&hl=pt_BR)")

                  


        st.markdown("---")


    with tab2:

        st.header("\U0001F393 Formação")        
        col4, col5 = st.columns(2)
        with st.container():
                with col4:
                    curso = st.subheader("Engenharia de Produção")
                    st.caption("Graduação")
                    inst = st.write(":office: Centro Universitário Jorge Amado")         
                    st.caption(":date: 2018 -2023")
                with col5:
                    curso = st.subheader("Engenharia de Sistemas e Produtos")
                    st.caption("Mestrado")
                    inst = st.write(":office: Instituto Federal de Educação, Ciência e Tecnologia da Bahia")                   
                    st.caption(":date: 2024 - 2026")

        st.markdown("---")

        st.header("\U0001F4BC Experiência Profissional")    
        col1, col2, col3 = st.columns(3)
        with st.container():
                with col1:
                    Função = st.subheader("Pesquisador Lider")
                    empresa = st.write(":office: Instituto Federal de Educação, Ciência e Tecnologia da Bahia")
                    st.caption(":date: 2024 - Atualmente")
                    st.caption("Lider de projetos de Pesquisa e Desenvolvimento (P&D) com foco em Qualidade e Análise de Riscos no departamento de Engenharia de Produtos e Sistemas.")

                with col2:
                    Função = st.subheader("Pesquisador/ Qualidade")
                    empresa = st.write(":office: IEL/ Ford Motor Company")
                    st.caption(":date: 2022 - 2025")
                    st.caption("Atuação em projetos de desenvolvimento organizacional com foco em testar e comprovar funcionalidades das áreas de Análise de Dados e Machine Learning em relação às ferramentas do setor de Engenharia de Qualidade objetivando sugerir melhorias que possam agregar mais valor para o cliente em relação à marca e trazer vantagem competitiva.")

                with col3:
                    Função = st.subheader("Instrutor de computação")
                    empresa = st.write(":office: Secretaria de Educação do Estado da Bahia")
                    st.caption(":date: 2021 - 2022")
                    st.caption("Execução de atividades de ensino e formação do curso de Programador de Sistemas do Programa Nacional de Acesso ao Ensino Técnico e Emprego (PRONATEC) em ambiente de sala de aula ou por meio de plataformas remotas. Atuando na criação de planos de aula, selecionando programas e materiais de referência necessários, explicando conceitos e teorias e corrigindo tarefas e provas. Demonstração de técnicas e ajuda em experimentos, pesquisas e projetos práticos relacionados com a área de programação de Sistemas.")


if __name__ == "__main__":
    main()