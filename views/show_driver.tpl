<table class="table table-striped">
    <thead>
    <tr>
        <th>Driver id</th>
        <th>Driver name</th>
        <th>Actions</th>
    </tr>
    </thead>
    <tbody>
    % for driver in list :
    <tr>
        <td>{{driver['driver_id']}}</td>
        <td>{{driver['driver_name']}}</td>
        <td>
            <a href="../../drivers/show/{{driver['driver_id']}}"><span
                    class="glyphicon glyphicon-eye-open"></span></a>
            <a href="../../drivers/form/update/{{driver['driver_id']}}"><span
                    class="glyphicon glyphicon-pencil"></span></a>
            <a href="../../drivers/delete/{{driver['driver_id']}}"><span
                    class="glyphicon glyphicon-trash"></span></a>
        </td>
    </tr>
    % end
    </tbody>
</table>
<a href="../../drivers/form/create">
    <button type="button" class="btn btn-success"><span class="glyphicon glyphicon-plus"></span></button>
</a>