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
                <div class="panel-heading"><h3><span class="glyphicon glyphicon-leaf"></span> Edit Car</h3></div>
                <div class="panel-body">
                    <form class="form-horizontal" method="post" action="/Car/update/{{Car['id']}}" id="car_form">
                         <a href="../../../Car">
                            <button type="button" class="btn btn-warning"><span class="glyphicon glyphicon-fast-backward"></span>  Back</button>
                        </a>
                        <a href="/Car/update/{{Car['id']}}">
                            <button type="submit" class="btn btn-success pull-right"><span class="glyphicon glyphicon-floppy-disk"></span> Save</button>
                        </a>
                        <h1></h1>
                        <div class="form-group">
                            <label class="col-sm-2">id</label>
                            <div class="col-sm-8">
                                <h5> {{Car['id']}} </h5>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="manufacturer_id" class="col-sm-2">manufacturer_id</label>
                            <div class="col-sm-8">
                                <select id='manufacturer_id' name='manufacturer_id' class="selectpicker"  title="{{Car['manufacturer_id']}}">
                                    % for Manufacturer in list :
                                        <option value="{{Manufacturer['id']}}">{{Manufacturer['id']}} : {{Manufacturer['name']}}</option>
                                    % end
                                </select>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="model" class="col-sm-2">model</label>
                            <div class="col-sm-8">
                                <input class="form-control" id="model" name='model' value="{{Car['model']}}"/>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="year" class="col-sm-2">year</label>
                            <div class="col-sm-8">
                                <input class="form-control" type='text' id="year" name='year' value="{{Car['year']}}"/>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="color" class="col-sm-2">color</label>
                            <div class="col-sm-8">
                                <input class="form-control" id="color" name='color' value="{{Car['color']}}"/>
                            </div>
                        </div>
                        <a href="/Car/delete/{{Car['id']}}">
                            <button type="button" class="btn btn-danger"><span class="glyphicon glyphicon-trash"></span> Delete</button>
                        </a>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
