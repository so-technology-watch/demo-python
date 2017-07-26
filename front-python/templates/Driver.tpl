<div class="container">
    <h2></h2>
    <div class="container">
        <div class="panel-group">
            <div class="panel panel-info">
                <div class="panel-heading"><h3><span class="glyphicon glyphicon-leaf"></span> Driver List</h3></div>
                <div class="panel-body">
                    <a href="../../../home">
                        <button type="button" class="btn btn-warning"><span class="glyphicon glyphicon-fast-backward"></span>  Back</button>
                    </a>
                    <a href="../../../../Driver/form/create" title="Create a new entity">
                        <button type="button" class="btn btn-success pull-right"><span class="glyphicon glyphicon-plus"></span> Create</button>
                    </a>
                    <h1></h1>
                    {{!footer}}
                    <h1></h1>
                    <table class="table table-striped table-bordered text-center">
                        <thead>
                        <tr>
                                <td><b>person</b></td>
                                <td><b>car</b></td>
                                <td><b>licence_number</b></td>
                                <td><b>licence_date</b></td>
                                <td><b>Actions</b></td>
                        </tr>
                        </thead>
                        <tbody>
                        % for Driver in list :
                        <tr>
                                <td>{{Driver['person_id']}}</td>
                                <td>{{Driver['car_id']}}</td>
                                <td>{{Driver['licence_number']}}</td>
                                <td>{{Driver['licence_date']}}</td>
                                <td>
                                <a href="../../../../Driver/show/{{Driver['person_id']}}/{{Driver['car_id']}}" title="Show this entity"><span
                                        class="glyphicon glyphicon-eye-open"></span></a>
                                <a href="../../../../Driver/form/update/{{Driver['person_id']}}/{{Driver['car_id']}}" title="Update this entity"><span
                                        class="glyphicon glyphicon-pencil"></span></a>
                                <a href="../../../../Driver/delete/{{Driver['person_id']}}/{{Driver['car_id']}}" title="Delete this entity"><span
                                        class="glyphicon glyphicon-trash"></span></a>
                            </td>
                        </tr>
                        % end
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</div>