class Api::Exposed::V1::UserCoursesController < Api::Exposed::V1::BaseController
  def index
    respond_with course.users, each_serializer: Api::Exposed::V1::UserCourseSerializer
  end

  def me
    respond_with current_user.courses_with_roles
  end

  def create
    respond_with new_user.add_role(user_course_params[:role], course)
  end

  def destroy
    respond_with new_user.remove_role(user_course_params[:role], course)
  end

  private

  def new_user
    @new_user ||= User.find_or_invite_by(email: user_course_params[:email])
  end

  def course
    @course ||= current_user.courses.friendly.find(params[:course_id])
  end

  def user_course_params
    params.require(:user_course).permit(
      :email,
      :role
    )
  end
end
