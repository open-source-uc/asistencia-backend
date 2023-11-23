class Api::Internal::ActivitiesController < Api::Internal::BaseController
  def index
    respond_with course.activities
  end

  def show
    respond_with activity
  end

  def create
    respond_with course.activities.create!(activity_params)
  end

  def update
    activity.update!(activity_params)
    respond_with activity
  end

  def destroy
    respond_with activity.destroy!
  end

  private

  def course
    @course ||= current_user.courses.friendly.find(params[:course_id])
  end

  def activity
    @activity ||= course.activities.find(params[:id])
  end

  def activity_params
    params.require(:activity).permit(
      :name,
      :description,
      :date,
      :slug
    )
  end
end
