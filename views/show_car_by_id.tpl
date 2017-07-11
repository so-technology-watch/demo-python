<table class="table table-stripped">
    <tr>
        <td>Car id :</td>
        <td>{{car['car_id']}}</td>
    </tr>
    <tr>
        <td>Car name :</td>
        <td>{{car['car_name']}}</td>
    </tr>
    <tr>
        <td>Driver :</td>
        <td>{{car['driver_id']}}</td>
    </tr>
</table>
<a href="/cars/delete/{{car['car_id']}}">
	<button type="button" class="btn btn-danger"><span class="glyphicon glyphicon-trash"></span> Delete</button>
</a>
<a href=/cars/form/update/{{car['car_id']}}>
	<button type="button" class="btn btn-info"><span class="glyphicon glyphicon-refresh"></span> Update</button>
</a>
