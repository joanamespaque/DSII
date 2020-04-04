let edit = $('.editar');
let close = $('.close');
inputnome = $('#nomepasta');
inputdesc = $('#descricaopasta');
secreto = $('.secretopasta');
formpasta = $('.formpasta');

close.click(function () {
    inputnome.val("");
    inputdesc.val("");
    $('#pastaid').remove();
    secreto.prop('checked', false);
});

$('.editar').click(function () {
    let id = $(this).attr('id');
    id = id.substr(6);
    req = $.ajax({
        url: '/pasta/buscar?id=' + id,
        type: 'GET',
        async: true,
        cache: true
    });
    req.done(function (data) {
        let pasta = JSON.parse(data.pasta);
        inputnome.val(pasta.nome);
        inputdesc.val(pasta.descricao);
        console.log(pasta.secreto);
        if (pasta.secreto == true) {
            secreto.attr("checked", "checked");
        }
        $('<input>').attr({
            type: 'hidden',
            id: 'pastaid',
            name: 'id',
            value: pasta.id
        }).appendTo(formpasta);
    });
});

$('.editar_pin').click(function() {
    let id =  $(this).attr('id');
    console.log("id: " + id);

    req = $.ajax({
        url: '/pin/buscar?id='+id,
        type: 'GET',
        async: true,
        cache: true
    });

    req.done(function(data) {
        let pin = JSON.parse(data.pin);
        console.log("pin: " + pin);
        console.log('pin titulo: ' + pin.titulo);
        $('#titulo').text("Título: " + pin.titulo);
        $('#descricao').text("Descrição: " + pin.descricao);
        $('#tematica').text("Temática: " + pin.tematica);
        $('#img_modal').attr("src", "/static/uploads/pins/" + pin.imagem);
    });
});