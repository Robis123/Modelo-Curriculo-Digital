
function jsAlterar(conhecimento, idt) {
    $("#fmAlterar" + idt).submit();
    $.post("/alterar", { idt: idt, nme: conhecimento }, function (retorno) {
        console.log(retorno);
    });
}

function jsExpor() {
    if ($('#formInclusao').css("display") == "none") {
        $('#formInclusao').slideDown("slow");
    } else {
        $('#formInclusao').slideUp("slow");
        //$('#formInclusao').css("display", "none");
    }
}
function jsExcluir(conhecimento, idt) {
    $("#fmExcluir" + idt).submit();
    var conf = confirm("Deseja excluir o conhecimento " + conhecimento + "?")
    if (!conf) {
        return
    }
    $.ajax({
        url: "/excluir",
        data: { idt: idt, nme: conhecimento },
        success: function (retorno) {
            $('#msg').css("display", "none");
            $("#msg").html(retorno);
            $('#msg').slideDown("slow");
            setInterval('location.reload(true)', 2000);
        }
    });
}

$.ajaxSetup({
    type: "POST"
});

// Desligar a submissão automática do formulário
$("#formulario").submit(function (event) {
    event.preventDefault();
});
$(".formalterar").submit(function (event) {
    event.preventDefault();
});
$(".formexcluir").submit(function (event) {
    event.preventDefault();
});

$("#fm").submit(function (event) {
    event.preventDefault();
});

// Chamar rota para incluir conhecimento
$('#incluir').click(function () {
    console.log("inawidnawiond");
    $('#formulario').submit();
    if ($('#inputConhecimento').val() != '') {
        $.ajax({
            url: "/incluir",
            data: { nme: $('#inputConhecimento').val(), dta: $('#inputData').val(), desc: $('#inputDesc').val() },
            success: function (retorno) {
                $('#msg').css("display", "none");
                $("#msg").html(retorno);
                $('#msg').slideDown("slow");
                setInterval('location.reload(true)', 2000);

            }
        });
    } else {
        alert("O campo conhecimento está em branco!");
    }
});






