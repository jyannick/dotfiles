(tool-bar-mode 0)
(set-frame-font "Fira Code 12" nil t)
(add-hook 'window-setup-hook 'toggle-frame-maximized t)


(require 'modus-themes)

;; Add all your customizations prior to loading the themes
(setq modus-themes-italic-constructs t
      modus-themes-bold-constructs nil
      modus-themes-region '(bg-only no-extend))

;; Load the theme files before enabling a theme
(modus-themes-load-themes)

;; Load the theme of your choice:
;; (modus-themes-load-operandi)
(modus-themes-load-vivendi)

(define-key global-map (kbd "<f5>") #'modus-themes-toggle)
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(inhibit-startup-screen t)
 '(package-selected-packages '(modus-themes)))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
