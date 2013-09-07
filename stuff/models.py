from django.db import models


class ParentWithDependentChildren(models.Model):
    """
    Model where the validation of child foreign-key relationships depends
    on validation of the parent
    """
    some_required_info = models.CharField(max_length=255)
    contingent_field = models.PositiveIntegerField(blank=True, default=1)
    
    class Meta:
        verbose_name_plural = "parents with dependent children"
        
    def __unicode__(self):
        return u'%s? +%d!' % (self.some_required_info, self.contingent_field)

    
class DependentChild(models.Model):
    """
    Model that depends on validation of the parent class for one of its
    fields to validate during clean
    """
    parent = models.ForeignKey(ParentWithDependentChildren)
    dependent_field = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = "dependent children"