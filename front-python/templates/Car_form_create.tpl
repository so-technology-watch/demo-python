<script>
    $(document).ready(function() {
        $('#car_form').bootstrapValidator({
            // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
            feedbackIcons: {
                valid: 'glyphicon glyphicon-ok',
                invalid: 'glyphicon glyphicon-remove',
                validating: 'glyphicon glyphicon-refresh'
            },
            fields: {
                model: {
                    validators: {
                            notEmpty: {
                            message: 'Model field is required'
                        }
                    }
                },
                year: {
                    validators: {
                            notEmpty: {
                            message: 'Year field is required'
                        }
                    }
                },
                manufacturer_id: {
                    validators: {
                            notEmpty: {
                            message: 'Please choose a Manufacturer_id'
                        },
                            notNull: {
                            message: 'Please choose a Manufacturer_id'
                        }
                    }
                }
            }
        })
    });
</script>

<div class="container">
    <h2></h2>
    <div class="container">
        <div class="panel-group">
            <div class="panel panel-info">
                <div class="panel-heading"><h3><span class="glyphicon glyphicon-leaf"></span> Create Car</h3></div>
                <div class="panel-body">
                    <form id="car_form" class="form-horizontal" method="post" action="/Car/create">
                        <a href="../../../Car">
                            <button type="button" class="btn btn-warning"><span class="glyphicon glyphicon-fast-backward"></span>  Back</button>
                        </a>
                         <a href="/Car/create">
                            <button type="submit" class="btn btn-success pull-right"><span class="glyphicon glyphicon-floppy-disk"></span> Save</button>
                        </a>
                        <h1></h1>
                        <div class="form-group">
                            <label for="id" class="col-sm-2">id</label>
                            <div class="col-sm-8">
                                <input class="form-control" id="id" name='id' value="auto value" disabled/>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="manufacturer_id" class="col-sm-2">manufacturer_id</label>
                            <div class="col-sm-8">
                                <select id='manufacturer_id' name='manufacturer_id' class="selectpicker" data-live-search="true">
                                    % for Manufacturer in list :
                                    <option title="{{Manufacturer['name']}}" value="{{Manufacturer['id']}}">{{Manufacturer['id']}} - {{Manufacturer['name']}}</option>
                                    % end
                                </select>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="model" class="col-sm-2">model</label>
                            <div class="col-sm-8">
                                <input class="form-control" id="model" name='model' value=""/>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="year" class="col-sm-2">year</label>
                            <div class="col-sm-8">
                                <input class="form-control" id="year" name='year' value="" type="text"/>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="color" class="col-sm-2">color</label>
                            <div class="col-sm-8">
                                <input class="form-control" id="color" name='color' value=""/>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>