<div class="container">
    <h2></h2>
    <div class="container">
        <div class="panel-group">
            <div class="panel panel-info">
                <div class="panel-heading"><h3><span class="glyphicon glyphicon-leaf"></span> Manufacturer List</h3></div>
                <div class="panel-body">
                    <a href="../../home">
                        <button type="button" class="btn btn-warning"><span class="glyphicon glyphicon-fast-backward"></span>  Back</button>
                    </a>
                    <a href="../../../../Manufacturer/form/create" title="Create a new entity">
                        <button type="button" class="btn btn-success pull-right"><span class="glyphicon glyphicon-plus"></span> Create</button>
                    </a>
                    <h1></h1>
                    {{!footer}}
                    <h1></h1>
                    <table class="table table-striped table-bordered text-center">
                        <thead>
                        <tr>
                                <td><b>id</b></td>
                                <td><b>name</b></td>
                                <td><b>Actions</b></td>
                        </tr>
                        </thead>
                        <tbody>
                        % for Manufacturer in list :
                        <tr>
                                <td>{{Manufacturer['id']}}</td>
                                <td>{{Manufacturer['name']}}</td>
                                <td>
                                <a href="../../../../Manufacturer/show/{{Manufacturer['id']}}" title="Show this entity"><span
                                        class="glyphicon glyphicon-eye-open"></span></a>
                                <a href="../../../../Manufacturer/form/update/{{Manufacturer['id']}}" title="Update this entity"><span
                                        class="glyphicon glyphicon-pencil"></span></a>
                                <a href="../../../../Manufacturer/delete/{{Manufacturer['id']}}" title="Delete this entity"><span
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