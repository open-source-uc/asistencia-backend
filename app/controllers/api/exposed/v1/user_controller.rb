class Api::Exposed::V1::UserController < Api::Exposed::V1::BaseController
  before_action :authenticate_user!

  def update
    respond_with current_user.update!(user_course_params)
  end

  def user_course_params
    params.require(:user).permit(
      :password,
      :password_confirmation
    )
  end
end
