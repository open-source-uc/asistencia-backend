Rails.application.routes.draw do
  scope path: '/api' do
    api_version(module: 'Api::Exposed::V1', path: { value: 'v1' }, defaults: { format: 'json' }) do
      resources :courses do
        resources :students do
          post 'batch_create', on: :collection
        end
        resources :activities
        resources :attendances
        post 'spreadsheets', to: 'spreadsheets#index'
        resource :user_courses, only: [] do
          get '/', to: 'user_courses#index'
          get 'me', on: :collection
          post 'batch_create', on: :collection
          post '/', to: 'user_courses#create'
          delete '/', to: 'user_courses#destroy'
        end
      end
    end
  end
  devise_for :admin_users, ActiveAdmin::Devise.config
  ActiveAdmin.routes(self)
  namespace :api, defaults: { format: :json } do
    namespace :internal do
    end
  end
  devise_for :users, controllers: { registrations: 'devise/registrations' }
  patch '/users/me', to: 'api/exposed/v1/user#update'
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"
end
