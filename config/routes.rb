Rails.application.routes.draw do
  scope path: '/api' do
    api_version(module: 'Api::Exposed::V1', path: { value: 'v1' }, defaults: { format: 'json' }) do
      resources :courses do
        resources :students
        resources :activities
        resources :attendances
      end
    end
  end
  devise_for :admin_users, ActiveAdmin::Devise.config
  ActiveAdmin.routes(self)
  namespace :api, defaults: { format: :json } do
    namespace :internal do
    end
  end
  devise_for :users
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"
end
