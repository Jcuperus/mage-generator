<?php

namespace MountainTales\Packing\Model\ResourceModel;

use Magento\Framework\Model\ResourceModel\Db\AbstractDb;

/**
 * Class {{ model }} Resource
 *
 * @package   MountainTales\Packing\Model\ResourceModel
 * @author    Jaep Cuperus <jaep@mountain-it.nl>
 * @copyright 24-4-19
 * @license   https://www.mountain-it.nl Commercial License
 */
class {{ model }} extends AbstractDb
{
    /**
     * {{ model }} resource constructor
     */
    protected function _construct()
    {
        $this->_init('{{ table }}', '{{ primary_key }}');
    }
}