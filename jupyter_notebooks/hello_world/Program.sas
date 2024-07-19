

proc sql;

	create table work.teste as
		select
			min(Limite_de_cr_dito) as min_Limite_de_cr_dito
			,max(Limite_de_cr_dito) as max_Limite_de_cr_dito
			,avg(Limite_de_cr_dito) as avg_Limite_de_cr_dito
			,median(Limite_de_cr_dito) as median_Limite_de_cr_dito
		from CREDITO.INDISPONIVEIS_20230404
	;

run;

proc univariate data=CREDITO.INDISPONIVEIS_20230404; 
var Limite_de_cr_dito; 
run; 