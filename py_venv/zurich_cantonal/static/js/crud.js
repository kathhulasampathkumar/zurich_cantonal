$(function () {

    // Start counting from the third row
    var counter = 2;

    $("#insertRow").on("click", function (event) {
        event.preventDefault();

        var newRow = $("<tr>");
        var cols = '';

        // Table columns
        cols += '<th scrope="row" name="srnum">' + counter + '</th>';
        cols += '<td><input type="text" name="date" id="inp'+counter+'" class="inputdate" required></td>';
        cols += '<td><select name="project" id="" style="width:60px";> <option value=""required>SELECT</option><option value="6FRA _ 6068">6FRA _ 6068</option><option value="9000 HP">9000 HP</option><option value="ALTERNATORS">ALTERNATORS</option><option value="DEMU">DEMU</option><option value="EMU">EMU</option><option value="EV PROJECT">EV PROJECT</option><option value="HIGH SPEED (Train-18)">HIGH SPEED (Train-18)</option><option value="KOLKATA METRO">KOLKATA METRO</option><option value="MEMU ON BOARD">MEMU ON BOARD</option><option value="MOSCOW">MOSCOW</option><option value="UNDER SLUNG EMU">UNDER SLUNG EMU</option><option value="UNDER SLUNG MEMU">UNDER SLUNG MEMU</option<option value="WDG4">WDG4</option>                                                                                                                                                                                                       </select></td>';
        cols += '<td><input type="text" name="compo" id=""  maxlength="12" class="compo1" required></td>';
        cols += '<td><input type="text" name="composr" id="" maxlength="12" style="width:100px" class="composr";required> </td>';
        cols += '<td><select name="rust" id="" style="width: 60px;"required>  <option value="">SELECT</option><option value="True">YES</option><option value="False">NO</option>   </select></td>';
        cols += '<td><select name="rotation" id="" style="width: 60px;"required>  <option value="">SELECT</option><option value="True">YES</option><option value="False">NO</option>  </select></td>';
        cols += '<td><select name="clean" id="" style="width: 60px;"required>  <option value="">SELECT</option><option value="True">YES</option><option value="False">NO</option>  </select></td>';
        cols += '<td><select name="cover" id="" style="width: 60px;"required>  <option value="">SELECT</option><option value="True">YES</option><option value="False">NO</option>  </select></td>';
        cols += '<td><input type="text" name="nextdate"id="due'+counter+'"class="nextdate"  onclick="datechange2('+counter+')" required></td>';
        cols += '<td><select name="dispatch" id="" style="width: 60px;"required>  <option value="">SELECT</option><option value=1>YES</option><option value=0>NO</option>  </select></td>';
        cols += '<td><i class="fa fa-trash"id ="deleteRow" style="font-size:20px;color:red;cursor:pointer; "></i></td>';

        // Insert the columns inside a row
        newRow.append(cols);

        // Insert the row inside a table
        $("table").append(newRow);

        // Increase counter after each row insertion
        counter++;
        $(".inputdate").datepicker(({
            dateFormat: 'yy-mm-dd',
            changeMonth: true,
            changeYear: true
        }));
        $(".nextdate").datepicker({
            dateFormat: 'yy-mm-dd',
            changeMonth: true,
            changeYear: true
        });
    });

    // Remove row when delete btn is clicked
    $("table").on("click", "#deleteRow", function (event) {
        $(this).closest("tr").remove();
         counter -= 1
    });



});

$(document).ready(function () {
    $(".inputdate").datepicker(({
        dateFormat: 'yy-mm-dd',
        changeMonth: true,
        changeYear: true
    }));
});

$(document).ready(function () {
    $(".nextdate").datepicker(({
        dateFormat: 'yy-mm-dd',
        changeMonth: true,
        changeYear: true
    }));
});


