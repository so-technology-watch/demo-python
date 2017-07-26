<script>
    $(document).ready(function() {
        $('#driver_form').bootstrapValidator({
            // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
            feedbackIcons: {
                valid: 'glyphicon glyphicon-ok',
                invalid: 'glyphicon glyphicon-remove',
                validating: 'glyphicon glyphicon-refresh'
            },
            fields: {
                licence_number: {
                    validators: {
                            notEmpty: {
                            message: 'Licence_number field is required'
                        }
                    }
                },
                licence_date: {
                    validators: {
                            notEmpty: {
                            message: 'Licence_date field is required'
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
                <div class="panel-heading"><h3><span class="glyphicon glyphicon-leaf"></span> Edit Driver </h3></div>
                <div class="panel-body">
					<form class="form-horizontal" method="post" action="/Driver/update/{{Driver['person_id']}}/{{Driver['car_id']}}" id="driver_form">
						<a href="../../../../Driver">
                            <button type="button" class="btn btn-warning"><span class="glyphicon glyphicon-fast-backward"></span>  Back</button>
                        </a>
						<a href="/Driver/update/{{Driver['person_id']}}/{{Driver['car_id']}}">
							<button type="submit" class="btn btn-success pull-right"><span class="glyphicon glyphicon-floppy-disk"></span> Save</button>
						</a>
						<h1></h1>
						<div class="form-group">
							<label for="person_id" class="col-sm-2">person_id</label>
							<div class="col-sm-8">
								<select id='person_id' name='person_id' class="selectpicker" data-live-search="true" multiple title="{{Driver['person_id']}}">
                                    % for Person in list :
                                    <option title="{{Person['lastname']}} {{Person['firstname']}}" value="{{Person['id']}}">{{Person['id']}} : {{Person['lastname']}} {{Person['firstname']}}</option>
                                    % end
                                </select>
							</div>
						</div>
						<div class="form-group">
							<label for="car_id" class="col-sm-2">car_id</label>
							<div class="col-sm-8">
								<select id='car_id' name='car_id' class="selectpicker" data-live-search="true" multiple title="{{Driver['car_id']}}">
                                    % for Car in list2 :
                                    <option title="{{Car['year']}} {{Car['model']}}" value="{{Car['id']}}">{{Car['id']}} : {{Car['year']}} {{Car['model']}}</option>
                                    % end
                                </select>
							</div>
						</div>
                        <div class="form-group">
							<label for="licence_number" class="col-sm-2">licence_number</label>
							<div class="col-sm-8">
								<input class="form-control" id="licence_number" name="licence_number" value="{{Driver['licence_number']}}"/>
							</div>
						</div>
						<div class="form-group">
							<label for="licence_date" class="col-sm-2">licence_date</label>
							<div class="col-sm-8">
								<input class="form-control" type='date' id="licence_date" name="licence_date" value="{{Driver['licence_date']}}"/>
							</div>
						</div>
						<a href="/Driver/delete/{{Driver['person_id']}}/{{Driver['car_id']}}">
							<button type="button" class="btn btn-danger"><span class="glyphicon glyphicon-trash"></span> Delete</button>
						</a>
					</form>
				</div>
			</div>
		</div>
	</div>
</div>