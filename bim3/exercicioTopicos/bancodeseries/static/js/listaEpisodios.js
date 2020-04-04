var cods = {}
    $('.seta').click(function() {
        let cod =  $(this).attr('id');
        cod = cod.substr(4);
        let r1 = $('.firstResponse'+cod);
        let r2 = $('.secondResponse'+cod);
        let loading = $('.loading'+cod)
        let img = document.createElement("IMG");
        img.src = "/static/img/carregar.gif";
        img.style.wcodth = "30px";
        img.style.height = "30px";
        if ((cod in cods) == false){
            loading.append(img);
            $.ajax({
                url: '/episodio/listar?cod='+cod,
                type: 'GET',
                async: true
            }).done(function(data) {
                let episodios = JSON.parse(data.episodios);
                let temporada = JSON.parse(data.temporada);
                console.log(episodios)
                console.log(temporada)
                cods[cod] = temporada.titulo;
                let count = Object.keys(episodios).length;
                loading.empty();
                thEP = document.createElement("th");
                thEP.innerHTML = "Episódios:";
                r1.append(thEP);   
                for(c = 0; c < count; c++){
                    tr1 = document.createElement("tr");
                    tr2 = document.createElement("tr");
                    for(i = Object.keys(episodios[c]).length-1; i > 0; i--){
                        th = document.createElement("th");
                        th.innerHTML = Object.keys(episodios[c])[i].toUpperCase();
                        tr1.append(th);
                        r2.append(tr1);
                    }
                    for(i = Object.keys(episodios[c]).length-1; i > 0; i--){
                        td = document.createElement("td");
                        td.innerHTML = Object.values(episodios[c])[i];
                        tr2.append(td);
                        r2.append(tr2);
                        
                    }
                }
            });
        } else{
            r1.empty();
            r2.empty();
            delete cods[cod];
        }
    });