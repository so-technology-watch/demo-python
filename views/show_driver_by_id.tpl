<table class="table table-stripped">
    <tr>
        <td>Driver id :</td>
        <td>{{driver['driver_id']}}</td>
    </tr>
    <tr>
        <td>Driver name :</td>
        <td>{{driver['driver_name']}}</td>
    </tr>
</table>
<a href="/drivers/delete/{{driver['driver_id']}}">
    <button type="button" class="btn btn-danger"><span class="glyphicon glyphicon-trash"></span> Delete</button>
</a>
<a href=/drivers/form/update/{{driver['driver_id']}}>
	<button type="button" class="btn btn-info"><span class="glyphicon glyphicon-refresh"></span> Update</button>
</a>
