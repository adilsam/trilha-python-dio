-- Por : Adilson Sampaio
create database ecommerce_alterado;
use ecommerce_alterado;
-- Tabelas que Representam Entidades

create table clientes (
	id_cliente int auto_increment primary key,
    nome_cliente varchar(100),
    CPF_cliente char(11) not null,
    endereco_cliente varchar(255),
    bairro_cliente varchar(50),
    estado_cliente char(2),
    email_cliente varchar(100),
    contato_cliente char(11),
    constraint unique_cpf_cliente unique (CPF_cliente)
);

create table produtos (
	id_produto int auto_increment primary key,
    nome_produto varchar(255) not null,
    categoria_produto enum('Eletrônico','Vestuário','Brinquedos','Alimentos','Móveis') not null
);

create table fornecedores (
	id_fornecedor int auto_increment primary key,
	razao_social_fornecedor varchar(255) not null,
	CNPJ_fornecedor char(15) not null,
	telefone_fornecedor char(11) not null,
	nome_contato_fornecedor varchar(100) not null,
    endereco_fornecedor varchar(100)not null,
    bairro_fornecedor varchar(50),
    estado_fornecedor char(2),
    cpf_contato_fornecedor char(11) not null,
	telefone_contato_fornecedor char(11) not null,
	constraint unique_cpf_contato_fornecedor unique (cpf_contato_fornecedor),
	constraint unique_cnpj_fornecedor unique (CNPJ_fornecedor)
);

create table pontos_venda (
	id_ponto_venda int auto_increment primary key,
	nome_pv varchar(100) not null,
	nome_responsavel_pv varchar(100) not null,
	endereco_pv varchar(255),
    bairro_pv varchar(50),
    estado_pv  char(2),
	contato_responsavel char(11) not null,
    constraint unique_nome_ponto_venda unique (nome_pv)
    );

-- Tabelas que Representam Relacionamentos entre Entidades
create table notas_fiscais_venda (
	id_nota_venda int auto_increment primary key,
	venda_Status enum('Cancelado','Confirmado','Em processamento') default 'Em processamento',
	descriccao_venda varchar(255),
	pagamento_tipo enum('Boleto','Crédito', 'Débito', 'Pix', 'Crediário', 'Cartão da Loja', 'Tranférência', 'dinheiro'),
	valor_total_nota_fiscal numeric(10,2),
	data_venda date not null
);

create table vendas (
	id_produto int,
	id_ordem_venda int not null auto_increment,
	id_nota_venda int,
	id_cliente int,
	quantidade_produto int not null,
	valor_unit numeric(10,2),
	total_venda numeric(10,2),
	constraint pk_vendas primary key (id_ordem_venda, id_nota_venda),
	constraint fk_vendas_produto foreign key (id_produto) references produtos(id_produto),
	constraint fk_vendas_nota_venda foreign key (id_nota_venda) references notas_fiscais_venda(id_nota_venda),
    constraint fk_vendas_cliente foreign key (id_cliente) references clientes(id_cliente)
);

create table compras (
	id_produto int,
	id_fornecedor int,
    data_compra date not null,
	quantidade_produto_comprado int not null,
    valor_unit numeric(10,2),
	total_compra numeric(10,2),
    constraint fk_compras_produto foreign key (id_produto) references produtos(id_produto),
    constraint fk_compras_fornecedor foreign key (id_fornecedor) references fornecedores(id_fornecedor)
);

create table estoque (
	id_estoque_produto int,
    id_estoque_pv int,
    quantidade_produto_pv int not null,
    constraint pk_estoque primary key (id_estoque_produto, id_estoque_pv),
    constraint fk_estoque_produto foreign key (id_estoque_produto) references produtos(id_produto),
    constraint fk_estoque_pv foreign key (id_estoque_pv) references pontos_venda(id_ponto_venda)
);
