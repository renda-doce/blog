#!/usr/bin/env python3
"""
SEO Optimization Script for Renda Doce Blog
Updates all HTML files with comprehensive SEO improvements.
"""

import re
from pathlib import Path

# Article metadata for structured data
ARTICLES = {
    "delivery-de-doces.html": {
        "title": "Do Zero à Primeira Venda: Como Montar um Delivery de Doces na Sua Cozinha",
        "description": "Guia completo para começar a vender bolos na marmita com baixo investimento. Renda extra na confeitaria de forma prática.",
        "image": "delivery-de-doces-capa.png",
        "keywords": "delivery de doces, bolo na marmita, ganhar dinheiro vendendo doces, negócio de confeitaria caseira"
    },
    "fidelizar-clientes-diabeticos.html": {
        "title": "Doces para Diabéticos: O Nicho que Vai Fidelizar sua Clientela",
        "description": "Aprenda a fazer bolos sem açúcar e low carb para conquistar um público fiel e diferenciado.",
        "image": "fidelizar-clientes-diabeticos.png",
        "keywords": "bolos para diabéticos, doces sem açúcar, confeitaria low carb, bolos fit"
    },
    "mini-bolos-vulcao.html": {
        "title": "Mini Vulcão: A Febre dos Bolos Individuais que Está Dominando o Mercado",
        "description": "Descubra os segredos do mini bolo vulcão: a sobremesa que une praticidade, beleza e muito lucro.",
        "image": "mini-bolos-vulcao-capa.png",
        "keywords": "mini vulcão, bolo vulcão individual, bolo recheado, doce para vender"
    },
    "slice-cakes.html": {
        "title": "Slice Cakes: Fatias de Bolo que Conquistam e Vendem Muito",
        "description": "Aprenda a fazer fatias de bolo recheadas e bem apresentadas, o produto perfeito para delivery.",
        "image": "slice-cakes-capa.png",
        "keywords": "slice cake, fatia de bolo gourmet, bolo fatiado, delivery de bolos"
    },
    "tortas-no-palito.html": {
        "title": "Tortas no Palito: A Lembrancinha Criativa que Encanta Festas",
        "description": "Pie pops são a nova tendência para lembrancinhas de festas. Aprenda técnicas e sabores que vendem.",
        "image": "tortas-no-palito-capa.png",
        "keywords": "torta no palito, pie pops, lembrancinha de festa, docinhos para festa"
    },
    "recheios-estruturados.html": {
        "title": "Recheios Estruturados: A Base de Todo Bolo de Festa Profissional",
        "description": "Domine a técnica de recheios firmes que não vazam e sustentam bolos altos e perfeitos.",
        "image": "recheios-estruturados-capa.png",
        "keywords": "recheio estruturado, recheio de bolo que não vaza, bolo de festa profissional"
    },
    "geladinho-gourmet.html": {
        "title": "Geladinho Gourmet: Lucre Alto no Verão com Ingredientes Simples",
        "description": "Sacolés cremosos e sabores premium para vender muito na estação mais quente do ano.",
        "image": "geladinho-gourmet-capa.png",
        "keywords": "geladinho gourmet, sacolé artesanal, negócio de verão, picolé caseiro"
    },
    "curso-de-donuts.html": {
        "title": "Donuts Americanos: A Tendência Colorida que Explodiu nas Redes",
        "description": "Aprenda a fazer donuts fofinhos, coloridos e irresistíveis que dominam as redes sociais.",
        "image": "curso-de-donuts-capa.png",
        "keywords": "donuts americanos, rosquinhas gourmet, donut caseiro, confeitaria moderna"
    },
    "panetones-artesanais.html": {
        "title": "Panetones Artesanais: Seu 13º Salário Vem do Natal",
        "description": "Domine a arte do panetone e chocotone trufado para faturar alto no fim do ano.",
        "image": "panetones-artesanais-capa.png",
        "keywords": "panetone artesanal, chocotone trufado, doces de natal, vender panetone"
    },
    "bolos-no-pote.html": {
        "title": "Fábrica de Bolos no Pote: O Negócio À Prova de Crise",
        "description": "Monte uma produção escalável de bolos no pote e venda todos os dias do ano.",
        "image": "bolos-no-pote-capa.png",
        "keywords": "bolo no pote, bolo de pote para vender, negócio lucrativo, confeitaria escalável"
    },
    "brigadeiros-gourmet.html": {
        "title": "Brigadeiros Gourmet: Eleve o Nível do Doce Mais Amado do Brasil",
        "description": "Transforme o brigadeiro tradicional em uma iguaria premium para festas e eventos.",
        "image": "brigadeiros-gourmet-capa.png",
        "keywords": "brigadeiro gourmet, doces finos, brigadeiro de festa, confeitaria premium"
    },
    "decoracao-com-bicos.html": {
        "title": "Decoração com Bicos: Transforme Bolos Simples em Obras de Arte",
        "description": "Domine a técnica do chantininho e crie decorações que valorizam seus bolos.",
        "image": "decoracao-com-bicos-capa.png",
        "keywords": "decoração com bicos, chantininho, bico de confeitar, cake design"
    },
    "bolo-no-palito.html": {
        "title": "Cake Pops: A Lembrancinha que as Crianças Amam",
        "description": "Bolos no palito coloridos e criativos para festas infantis e eventos.",
        "image": "bolo-no-palito-capa.png",
        "keywords": "cake pops, bolo no palito, lembrancinha infantil, doce para festa"
    },
    "tortas-de-confeitaria.html": {
        "title": "Tortas de Vitrine: Banoffee, Limão e Outros Clássicos Elegantes",
        "description": "Aprenda as tortas clássicas de confeitaria que vendem pela sofisticação.",
        "image": "tortas-de-confeitaria-capa.png",
        "keywords": "torta de limão, banoffee, tortas clássicas, doces elegantes"
    },
    "frutas-confeitaria-moderna.html": {
        "title": "Frutas Frescas na Confeitaria: Leveza e Beleza Natural",
        "description": "Use frutas frescas para criar sobremesas modernas, leves e Instagram-worthy.",
        "image": "frutas-confeitaria-moderna-capa.png",
        "keywords": "frutas na confeitaria, bolo com frutas, sobremesa saudável, confeitaria moderna"
    },
    "mini-vulcoes-low-carb.html": {
        "title": "Mini Vulcões Low Carb: O Melhor dos Dois Mundos",
        "description": "Atenda o público fitness com mini vulcões sem culpa e muito sabor.",
        "image": "mini-vulcoes-low-carb-capa.png",
        "keywords": "vulcão low carb, bolo fit, doce sem açúcar, confeitaria saudável"
    },
    "escola-de-bolos-caseiros.html": {
        "title": "Escola de Bolos Caseiros: O Sabor da Infância que Vende Todo Dia",
        "description": "Aprenda a fazer bolos caseiros fofinhos e lucrativos. O negócio perfeito para começar na cozinha da sua casa.",
        "image": "escola-de-bolos-caseiros-capa.png",
        "keywords": "bolo caseiro, bolo de fubá, bolo de milho, bolos tradicionais"
    },
    "sobremesas-lucrativas.html": {
        "title": "Sobremesas Lucrativas: Diversifique seu Cardápio e Aumente o Ticket Médio",
        "description": "Apostila de Sobremesas Lucrativas. Receitas práticas e econômicas para vender no delivery ou em potes.",
        "image": "sobremesas-lucrativas-capa.png",
        "keywords": "pudim caseiro, mousse, pavê, sobremesas geladas"
    },
    "bolos-juninos.html": {
        "title": "Bolos Juninos: A Temporada Mais Gostosa e Lucrativa do Ano",
        "description": "Aprenda a lucrar com as Festas Juninas. Bolos de milho, fubá, amendoim e mandioca que vendem muito em junho e julho.",
        "image": "bolos-juninos-capa.png",
        "keywords": "bolo de milho, bolo de fubá, festa junina, doces de são joão"
    },
    "vitrine-bolos-classicos.html": {
        "title": "Vitrine de Bolos Clássicos: A Elegância que Nunca Sai de Moda",
        "description": "Aprenda a fazer os bolos icônicos que encantam gerações. Floresta Negra, Marta Rocha e muito mais.",
        "image": "vitrine-bolos-classicos-capa.png",
        "keywords": "floresta negra, marta rocha, bolos clássicos, confeitaria tradicional"
    },
    "vivendo-de-bolos-vulcoes.html": {
        "title": "Vivendo de Bolos Vulcões: Como Transformar uma Tendência em Negócio Sólido",
        "description": "Transforme a produção de Bolos Vulcão em sua fonte de renda principal. Estratégias de venda e produção.",
        "image": "vivendo-de-bolos-vulcoes-capa.png",
        "keywords": "viver de confeitaria, negócio de bolos, empreendedorismo, bolo vulcão"
    },
    "bolos-gelados-lucrativos.html": {
        "title": "Bolos Gelados Lucrativos: O Retorno Triunfal do Bolo Embrulhado",
        "description": "Aprenda a fazer Bolos Gelados embrulhados. O clássico bolo de coco e novas versões gourmet para vender muito.",
        "image": "bolos-gelados-lucrativos-capa.png",
        "keywords": "bolo gelado, bolo de coco, bolo embrulhado, toalha felpuda"
    },
    "colecao-receitas-lucrativas.html": {
        "title": "Coleção Receitas Lucrativas: O Arsenal Completo da Confeiteira de Sucesso",
        "description": "Tenha acesso às receitas mais vendidas da Chef Isis. Uma coleção completa para alavancar seu negócio.",
        "image": "colecao-receitas-lucrativas-capa.png",
        "keywords": "receitas de bolos, apostila de confeitaria, fichas técnicas, receitas lucrativas"
    },
    "sobremesas-2025.html": {
        "title": "Sobremesas 2025: O Futuro da Confeitaria Começa Agora",
        "description": "Antecipe as tendências da confeitaria para 2025. Sobremesas modernas, novos sabores e técnicas que vão bombar.",
        "image": "sobremesas-2025-capa.png",
        "keywords": "tendências confeitaria, sobremesas modernas, inovação em doces, confeitaria 2025"
    }
}

def create_seo_head(filename, metadata, base_url="https://rendadoce.blog"):
    """Generate comprehensive SEO head section."""
    canonical = f"{base_url}/{filename}"
    image_url = f"{base_url}/img/{metadata['image']}"
    
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{metadata['description']}">
    <meta name="keywords" content="{metadata['keywords']}">
    <meta name="author" content="Renda Doce">
    
    <!-- Canonical URL -->
    <link rel="canonical" href="{canonical}">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="{canonical}">
    <meta property="og:title" content="{metadata['title']}">
    <meta property="og:description" content="{metadata['description']}">
    <meta property="og:image" content="{image_url}">
    <meta property="og:site_name" content="Renda Doce">
    <meta property="og:locale" content="pt_BR">
    
    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:url" content="{canonical}">
    <meta name="twitter:title" content="{metadata['title']}">
    <meta name="twitter:description" content="{metadata['description']}">
    <meta name="twitter:image" content="{image_url}">
    
    <title>{metadata['title']} | Renda Doce</title>
    
    <!-- Self-hosted Fonts and Styles -->
    <link rel="stylesheet" href="style.css">
    
    <!-- Structured Data (JSON-LD) -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{metadata['title']}",
      "description": "{metadata['description']}",
      "image": "{image_url}",
      "author": {{
        "@type": "Organization",
        "name": "Renda Doce"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "Renda Doce",
        "logo": {{
          "@type": "ImageObject",
          "url": "{base_url}/img/logo.png"
        }}
      }},
      "datePublished": "2025-11-25",
      "dateModified": "2025-11-25",
      "mainEntityOfPage": {{
        "@type": "WebPage",
        "@id": "{canonical}"
      }}
    }}
    </script>
</head>'''

def update_html_file(filepath):
    """Update a single HTML file with SEO improvements."""
    filename = filepath.name
    
    if filename not in ARTICLES:
        return False
    
    content = filepath.read_text(encoding='utf-8')
    metadata = ARTICLES[filename]
    
    # Find the end of the head section
    head_match = re.search(r'</head>', content, re.IGNORECASE)
    if not head_match:
        return False
    
    # Extract body content (everything from <body> onwards)
    body_match = re.search(r'<body.*?>.*', content, re.DOTALL | re.IGNORECASE)
    if not body_match:
        return False
    
    body_content = body_match.group(0)
    
    # Create new HTML with optimized head
    new_head = create_seo_head(filename, metadata)
    new_html = f"{new_head}\n{body_content}"
    
    # Write updated content
    filepath.write_text(new_html, encoding='utf-8')
    return True

def main():
    blog_dir = Path('/home/roberto/00-renda-doce/blog')
    updated_count = 0
    
    for filename in ARTICLES.keys():
        filepath = blog_dir / filename
        if filepath.exists():
            if update_html_file(filepath):
                print(f"✓ Updated: {filename}")
                updated_count += 1
            else:
                print(f"✗ Failed: {filename}")
        else:
            print(f"✗ Not found: {filename}")
    
    print(f"\n{updated_count}/{len(ARTICLES)} files updated successfully!")

if __name__ == "__main__":
    main()
