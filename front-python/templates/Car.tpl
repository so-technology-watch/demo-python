<div class="container">
    <h2></h2>
    <div class="container">
        <div class="panel-group">
            <div class="panel panel-info">
                <div class="panel-heading"><h3><span class="glyphicon glyphicon-leaf"></span> Car List</h3></div>
                <div class="panel-body">
                    <a href="../../home">
                        <button type="button" class="btn btn-warning"><span class="glyphicon glyphicon-fast-backward"></span>  Back</button>
                    </a>
                    <a href="../../../../Car/form/create" title="Create a new entity">
                        <button type="button" class="btn btn-success pull-right"><span class="glyphicon glyphicon-plus"></span> Create</button>
                    </a>
                    <h1></h1>
                    {{!footer}}
                    <table class="table table-striped table-bordered text-center">
                        <thead>
                        <tr>
                                <td><b>id</b></td>
                                <td><b>manufacturer</b></td>
                                <td><b>model</b></td>
                                <td><b>year</b></td>
                                <td><b>color</b></td>
                                <td><b>Actions</b></td>
                        </tr>
                        </thead>
                        <tbody>
                        % for Car in list :
                        <tr>
                                <td>{{Car['id']}}</td>
                                <td>{{Car['manufacturer_id']}}</td>
                                <td>{{Car['model']}}</td>
                                <td>{{Car['year']}}</td>
                                <td>{{Car['color']}}</td>
                                <td>
                                <a href="../../../../Car/show/{{Car['id']}}" title="Show this entity"><span
                                        class="glyphicon glyphicon-eye-open"></span></a>
                                <a href="../../../../Car/form/update/{{Car['id']}}" title="Update this entity"><span
                                        class="glyphicon glyphicon-pencil"></span></a>
                                <a href="../../../../Car/delete/{{Car['id']}}" title="Delete this entity"><span
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




