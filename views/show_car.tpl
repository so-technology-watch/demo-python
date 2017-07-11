<table class="table table-striped">
    <thead>
    <tr>
        <th>Car id</th>
        <th>Car name</th>
        <th>Driver id</th>
        <th>Actions</th>
    </tr>
    </thead>
    <tbody>
    % for car in list :
    <tr>
        <td>{{car['car_id']}}</td>
        <td>{{car['car_name']}}</td>
        <td>{{car['driver_id']}}</td>
        <td>
            <a href="../../cars/show/{{car['car_id']}}"><span
                    class="glyphicon glyphicon-eye-open"></span></a>
            <a href="../../cars/form/update/{{car['car_id']}}"><span
                    class="glyphicon glyphicon-pencil"></span></a>
            <a href="../../cars/delete/{{car['car_id']}}"><span
                    class="glyphicon glyphicon-trash"></span></a>
        </td>
    </tr>
    % end
    </tbody>
</table>
<a href="../../cars/form/create">
    <button type="button" class="btn btn-success"><span class="glyphicon glyphicon-plus"></span> Create</button>
</a>